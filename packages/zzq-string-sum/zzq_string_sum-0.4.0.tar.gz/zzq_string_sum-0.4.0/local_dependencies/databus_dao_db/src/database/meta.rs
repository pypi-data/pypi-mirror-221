use crate::DBManager;
use anyhow::Context;
use async_trait::async_trait;
use databus_core::types::Json;
use mysql_async::params;
use std::sync::Arc;

#[async_trait]
pub trait DatasheetMetaDAO: Send + Sync {
  async fn get_meta_data_by_dst_id(&self, dst_id: &str, include_deleted: bool) -> anyhow::Result<Option<Json>>;
}

struct DatasheetMetaDAOImpl {
  repo: Arc<dyn DBManager>,
}

pub fn new_dao(repo: Arc<dyn DBManager>) -> Arc<dyn DatasheetMetaDAO> {
  Arc::new(DatasheetMetaDAOImpl { repo })
}

#[async_trait]
impl DatasheetMetaDAO for DatasheetMetaDAOImpl {
  async fn get_meta_data_by_dst_id(&self, dst_id: &str, include_deleted: bool) -> anyhow::Result<Option<Json>> {
    let mut client = self.repo.get_client().await?;
    let mut query = format!(
      "
      SELECT `meta_data` \
      FROM `{prefix}datasheet_meta` \
      WHERE `dst_id` = :dst_id",
      prefix = self.repo.table_prefix()
    );
    if !include_deleted {
      query.push_str(" AND is_deleted = 0");
    }
    Ok(
      client
        .query_one(
          query,
          params! {
            dst_id
          },
        )
        .await
        .with_context(|| format!("get datasheet meta data of {dst_id}"))?,
    )
  }
}

#[cfg(test)]
pub mod mock {
  use super::*;
  use databus_core::types::HashMap;

  #[derive(Default)]
  pub struct MockDatasheetMetaDAOImpl {
    metas: HashMap<&'static str, Json>,
  }

  impl MockDatasheetMetaDAOImpl {
    pub fn new() -> Self {
      Self::default()
    }

    pub fn with_metas(mut self, metas: HashMap<&'static str, Json>) -> Self {
      self.metas = metas;
      self
    }

    pub fn build(self) -> Arc<dyn DatasheetMetaDAO> {
      Arc::new(self)
    }
  }

  #[async_trait]
  impl DatasheetMetaDAO for MockDatasheetMetaDAOImpl {
    async fn get_meta_data_by_dst_id(&self, dst_id: &str, _include_deleted: bool) -> anyhow::Result<Option<Json>> {
      Ok(self.metas.get(dst_id).cloned())
    }
  }
}
