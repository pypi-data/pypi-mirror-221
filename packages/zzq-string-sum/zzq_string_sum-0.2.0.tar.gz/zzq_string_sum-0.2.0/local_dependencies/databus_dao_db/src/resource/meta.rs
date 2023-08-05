use crate::DBManager;
use anyhow::Context;
use async_trait::async_trait;
use mysql_async::params;
use std::sync::Arc;

#[async_trait]
pub trait ResourceMetaDAO: Send + Sync {
  async fn get_revision_by_res_id(&self, res_id: &str) -> anyhow::Result<Option<u64>>;
}

struct ResourceMetaDAOImpl {
  repo: Arc<dyn DBManager>,
}

pub fn new_dao(repo: Arc<dyn DBManager>) -> Arc<dyn ResourceMetaDAO> {
  Arc::new(ResourceMetaDAOImpl { repo })
}

#[async_trait]
impl ResourceMetaDAO for ResourceMetaDAOImpl {
  async fn get_revision_by_res_id(&self, res_id: &str) -> anyhow::Result<Option<u64>> {
    let mut client = self.repo.get_client().await?;
    Ok(
      client
        .query_one(
          format!(
            "\
              SELECT `revision` \
              FROM `{prefix}resource_meta` \
              WHERE `resource_id` = :res_id AND `is_deleted` = 0\
            ",
            prefix = self.repo.table_prefix()
          ),
          params! {
            res_id
          },
        )
        .await
        .with_context(|| format!("get revision by resource id {res_id}"))?,
    )
  }
}
