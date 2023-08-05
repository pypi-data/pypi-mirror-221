use anyhow::{anyhow, Context};
use async_trait::async_trait;
use databus_core::errors::{RestError, ServerError};
use databus_core::types::Json;
use databus_core::types::JsonExt;
use databus_core::types::{AuthHeader, HttpSuccessResponse, NodePermission};
use futures::future::BoxFuture;
use futures::TryFutureExt;
use serde::de::DeserializeOwned;
use serde_json::json;
use std::sync::Arc;
use surf::http::Method;
use surf::Url;

pub struct HttpClient(surf::Client);

#[async_trait]
pub trait RestDAO: Send + Sync {
  async fn get_node_permission(
    &self,
    auth: &AuthHeader,
    node_id: &str,
    share_id: Option<&str>,
  ) -> anyhow::Result<NodePermission>;

  async fn get_field_permission(
    &self,
    auth: &AuthHeader,
    node_id: &str,
    share_id: Option<&str>,
  ) -> anyhow::Result<Json>;

  async fn has_login(&self, cookie: &str) -> anyhow::Result<bool>;
}

struct RestDAOImpl {
  http_client: HttpClient,
}

pub fn new_dao(base_url: String) -> Arc<dyn RestDAO> {
  Arc::new(RestDAOImpl {
    http_client: HttpClient::new(base_url),
  })
}

#[async_trait]
impl RestDAO for RestDAOImpl {
  async fn get_node_permission(
    &self,
    auth: &AuthHeader,
    node_id: &str,
    share_id: Option<&str>,
  ) -> anyhow::Result<NodePermission> {
    self
      .http_client
      .get(
        format!("internal/node/{node_id}/permission"),
        auth,
        share_id.map(|share_id| json!({ "shareId": share_id })),
      )
      .await
      .map(|resp| resp.data)
  }

  async fn get_field_permission(
    &self,
    auth: &AuthHeader,
    node_id: &str,
    share_id: Option<&str>,
  ) -> anyhow::Result<Json> {
    self
      .http_client
      .get(
        format!("internal/node/{node_id}/field/permission"),
        auth,
        Some(json!({
          "shareId": share_id,
          "userId": auth.user_id,
        })),
      )
      .await
      .and_then(|resp| {
        Json::into_prop(resp.data, "fieldPermissionMap").map_err(|data| anyhow!("missing fieldPermissionMap: {data:?}"))
      })
  }

  async fn has_login(&self, cookie: &str) -> anyhow::Result<bool> {
    self
      .http_client
      .get(
        "internal/user/session",
        &AuthHeader {
          cookie: Some(cookie.to_owned()),
          ..Default::default()
        },
        None,
      )
      .await
      .map(|resp| resp.data)
  }
}

fn http_log(
  req: surf::Request,
  client: surf::Client,
  next: surf::middleware::Next,
) -> BoxFuture<surf::Result<surf::Response>> {
  Box::pin(async move {
    let url = req.url().to_string();
    tracing::info!("Remote call address: {url}");
    let result = next.run(req, client).await;
    if let Err(err) = &result {
      tracing::error!("Remote call {url} failed: {err}");
    }
    result
  })
}

impl HttpClient {
  fn new<S>(base_url: S) -> Self
  where
    S: AsRef<str>,
  {
    let client: surf::Client = surf::Config::new()
      .set_base_url(Url::parse(base_url.as_ref()).unwrap())
      .add_header("X-Internal-Request", "yes")
      .unwrap()
      .try_into()
      .unwrap();
    Self(client.with(http_log))
  }

  async fn get<S, T>(&self, url: S, auth: &AuthHeader, query: Option<Json>) -> anyhow::Result<HttpSuccessResponse<T>>
  where
    S: AsRef<str>,
    T: DeserializeOwned,
  {
    self.request(Method::Get, url, auth, query, None).await
  }

  async fn request<S, T>(
    &self,
    method: Method,
    url: S,
    auth: &AuthHeader,
    query: Option<Json>,
    body: Option<Json>,
  ) -> anyhow::Result<HttpSuccessResponse<T>>
  where
    T: DeserializeOwned,
    S: AsRef<str>,
  {
    let url = url.as_ref();
    let mut req_builder = self.0.request(method, url);

    if let Some(cookie) = &auth.cookie {
      req_builder = req_builder.header("Cookie", cookie);
    } else if let Some(token) = &auth.token {
      req_builder = req_builder.header("Authorization", token);
    }

    if let Some(query) = query {
      req_builder = req_builder
        .query(&query)
        .map_err(|err| err.into_inner())
        .with_context(|| format!("add query {query:?} for server request {url}"))?;
    }

    if let Some(body) = body {
      req_builder = req_builder
        .body_json(&body)
        .map_err(|err| err.into_inner())
        .with_context(|| format!("add body for server request {url}"))?;
    }

    let req = req_builder.build();
    let url = req.url().to_string();

    let resp = self
      .0
      .send(req)
      .and_then(move |mut resp| async move { resp.body_json::<HttpSuccessResponse<T>>().await })
      .map_err(|err| err.into_inner())
      .await
      .with_context(|| format!("server request {url}"))?;

    if resp.success {
      return Ok(resp);
    }

    tracing::error!(
      "Remote call {url} failed, error code:[{}], error:[{}]`);",
      resp.code,
      resp.message,
    );

    if let 201 | 403 | 600 | 601 | 602 | 404 | 411 = resp.code {
      return Err(
        RestError {
          status_code: resp.code as u16,
        }
        .into(),
      );
    }

    Err(ServerError.into())
  }
}

#[cfg(test)]
pub mod mock {
  use super::*;
  use anyhow::anyhow;
  use databus_core::types::{HashMap, HashSet};

  #[derive(Default)]
  pub struct MockRestDAOImpl {
    node_permissions: HashMap<(&'static str, Option<&'static str>), NodePermission>,
    field_permissions: HashMap<(&'static str, Option<&'static str>), Json>,
    logined: HashSet<&'static str>,
  }

  impl MockRestDAOImpl {
    pub fn new() -> Self {
      Self::default()
    }

    pub fn with_node_permissions(
      mut self,
      node_permissions: HashMap<(&'static str, Option<&'static str>), NodePermission>,
    ) -> Self {
      self.node_permissions = node_permissions;
      self
    }

    #[allow(unused)]
    pub fn with_field_permissions(
      mut self,
      field_permissions: HashMap<(&'static str, Option<&'static str>), Json>,
    ) -> Self {
      self.field_permissions = field_permissions;
      self
    }

    #[allow(unused)]
    pub fn with_logined(mut self, logined: HashSet<&'static str>) -> Self {
      self.logined = logined;
      self
    }

    pub fn build(self) -> Arc<dyn RestDAO> {
      Arc::new(self)
    }
  }

  #[async_trait]
  impl RestDAO for MockRestDAOImpl {
    async fn get_node_permission(
      &self,
      _auth: &AuthHeader,
      node_id: &str,
      share_id: Option<&str>,
    ) -> anyhow::Result<NodePermission> {
      self
        .node_permissions
        .get(&(node_id, share_id))
        .cloned()
        .ok_or_else(|| anyhow!("node permission ({node_id}, {share_id:?}) not exist"))
    }

    async fn get_field_permission(
      &self,
      _auth: &AuthHeader,
      node_id: &str,
      share_id: Option<&str>,
    ) -> anyhow::Result<Json> {
      self
        .field_permissions
        .get(&(node_id, share_id))
        .cloned()
        .ok_or_else(|| anyhow!("field permission ({node_id}, {share_id:?}) not exist"))
    }

    async fn has_login(&self, cookie: &str) -> anyhow::Result<bool> {
      Ok(self.logined.contains(cookie))
    }
  }
}
