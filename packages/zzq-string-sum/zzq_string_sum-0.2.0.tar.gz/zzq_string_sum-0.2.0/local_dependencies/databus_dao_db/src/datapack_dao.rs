use crate::{DBManager, DBManagerImpl, RepositoryInitOptions};
use anyhow::Context;
use async_trait::async_trait;
use databus_core::types::DatasheetPack;
use databus_core::types::{AuthHeader, FetchDataPackOptions, FetchDataPackOrigin};
use fred::prelude::*;
use std::fmt::{self, Display, Formatter};
use std::sync::Arc;

#[async_trait]
pub trait DataPackDAO: Send + Sync {
  async fn fetch_datasheet_pack(
    &self,
    source: &str,
    dst_id: &str,
    auth: AuthHeader,
    origin: FetchDataPackOrigin,
    options: Option<FetchDataPackOptions>,
  ) -> anyhow::Result<DatasheetPack>;

  async fn destroy(&self) -> anyhow::Result<()>;
}

struct DataPackDAOImpl {
  datasheet_dao: Arc<crate::database::datasheet::DatasheetDAO>,
  repo: Arc<dyn DBManager>,
}

#[derive(Debug, Clone)]
pub struct RedisOptions {
  pub username: Option<String>,
  pub password: Option<String>,
  pub host: String,
  pub port: u16,
  pub database: Option<u8>,
}

impl From<RedisOptions> for RedisConfig {
  fn from(value: RedisOptions) -> Self {
    Self {
      username: value.username,
      password: value.password,
      server: ServerConfig::Centralized {
        server: (value.host, value.port).into(),
      },
      database: value.database,
      ..Default::default()
    }
  }
}

#[derive(Debug, Clone)]
pub struct MysqlOptions {
  pub username: String,
  pub password: String,
  pub host: String,
  pub port: u16,
  pub database: String,
}

impl Display for MysqlOptions {
  fn fmt(&self, f: &mut Formatter) -> fmt::Result {
    write!(
      f,
      "mysql://{user}:{password}@{host}:{port}/{database}",
      user = url_escape::encode_component(&self.username),
      password = url_escape::encode_component(&self.password),
      host = self.host,
      port = self.port,
      database = self.database,
    )
  }
}

#[derive(Debug, Clone)]
pub struct DataPackDAOOptions {
  pub redis: RedisOptions,
  pub mysql: MysqlOptions,
  pub rest_api_base_url: String,
  pub oss_host: String,
  pub table_prefix: String,
}

impl DataPackDAOOptions {
  pub async fn init(self) -> anyhow::Result<Arc<dyn DataPackDAO>> {
    // databus_core::new_repository(
    let repo = DBManagerImpl::get_instance(RepositoryInitOptions {
      conn_url: self.mysql.to_string(),
      table_prefix: self.table_prefix,
    });

    repo.init().await.context("init repository")?;

    let datasheet_meta_dao = crate::database::meta::new_dao(repo.clone());

    let resource_meta_dao = crate::resource::meta::new_dao(repo.clone());

    let datasheet_record_comment_dao = crate::database::record_comment::new_dao(repo.clone());

    let node_desc_dao = crate::node::description::new_dao(repo.clone());

    let redis_dao = crate::redis::new_dao(self.redis.into()).await.context("init redis")?;

    // let str = redis_dao.get_connection().await.unwrap().get::<String, _>("foo").await?;
    // println!("let's see str: {:?}", str);
    // match redis_dao
    //     .get_connection().await.unwrap()
    //     .sismember::<bool,_,_>( "vikadata:nest:fieldReRef:dstgsxQiDzw1Q3Hjhr:fldDqDXIHInvq", "dstjL5eP37l5vY8ERJ:fldDkurLV1XhO")
    //     .await {
    //   Ok(r) => { println!("have load r1 {}", r);}
    //   Err(e) => { println!("have load e1 {:?}", e);}
    // }
    let rest_dao = crate::rest::new_dao(self.rest_api_base_url);

    let unit_dao = crate::unit::new_dao(self.oss_host.clone(), repo.clone());

    let user_dao = crate::user::new_dao(rest_dao.clone(), repo.clone(), self.oss_host.clone());

    let node_children_dao = crate::node::children::new_dao(repo.clone());

    let node_share_setting_dao = crate::node::share_setting::new_dao(repo.clone(), node_children_dao.clone());

    let node_perm_dao = crate::node::permission::new_dao(
      repo.clone(),
      node_share_setting_dao.clone(),
      rest_dao.clone(),
      user_dao.clone(),
    );

    let datasheet_revision_dao = crate::database::revision::new_dao(repo.clone());

    let node_dao = crate::node::node::new_dao(
      repo.clone(),
      resource_meta_dao.clone(),
      datasheet_revision_dao.clone(),
      node_desc_dao.clone(),
      node_perm_dao.clone(),
      node_share_setting_dao.clone(),
    );

    let record_dao = crate::database::record::new_dao(repo.clone(), datasheet_record_comment_dao.clone());

    let datasheet_dao = crate::database::datasheet::new_dao(
      datasheet_meta_dao,
      record_dao,
      node_dao,
      datasheet_revision_dao,
      user_dao,
      unit_dao,
      redis_dao,
      repo.clone(),
    );

    Ok(Arc::new(DataPackDAOImpl {
      datasheet_dao: datasheet_dao,
      repo: repo.clone(),
    }))
  }
}

#[async_trait]
impl DataPackDAO for DataPackDAOImpl {
  async fn fetch_datasheet_pack(
    &self,
    source: &str,
    dst_id: &str,
    auth: AuthHeader,
    origin: FetchDataPackOrigin,
    options: Option<FetchDataPackOptions>,
  ) -> anyhow::Result<DatasheetPack> {
    self
      .datasheet_dao
      .fetch_data_pack(source, dst_id, auth, origin, options)
      .await
  }

  async fn destroy(&self) -> anyhow::Result<()> {
    self.repo.close().await?;
    Ok(())
  }
}
