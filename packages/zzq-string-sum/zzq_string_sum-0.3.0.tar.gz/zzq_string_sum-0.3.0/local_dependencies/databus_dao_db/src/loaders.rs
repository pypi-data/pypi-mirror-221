use databus_core::types::DatasheetPack;

use databus_core::types::AuthHeader;

use databus_core::types::FetchDataPackOrigin;
use databus_core::types::IDatasheetPackLoader;

use async_trait::async_trait;
use std::sync::Arc;

use crate::DataPackDAO;
use crate::DataPackDAOOptions;
use crate::RedisOptions;
// use crate::DataPackDAOOptions;
// use crate::RedisOptions;
// use crate::DataPackDAOOptions;
// use crate::RedisOptions;

use databus_core::types::ResultExt;

// use crate::so::types::Record;
// use databus_core::types::DatasheetPack;

// use super::data_bundle::DataBundle;
use tokio::runtime::Runtime;
use once_cell::sync::OnceCell;

static TOKIO_RUNTIME: OnceCell<Runtime> = OnceCell::new();

/**
 * Load Snapshot via MySQL / Databases.
 * Especially for backend.
 */
pub struct DBLoader {
  dao: Arc<dyn DataPackDAO>,
}

impl DBLoader {

  pub async fn ainit() -> DBLoader {
    let rest_base_url = env_var!(REST_BASE_URL default "http://localhost:8081/api/v1/");
    let dao_options = get_dao_options(rest_base_url);
    let result = dao_options.init().await;

    tracing::info!("database loader init successfully");
    return DBLoader { dao: result.unwrap() };
  }

  pub fn init() -> DBLoader {
    let rt = TOKIO_RUNTIME.get_or_init(|| {
      Runtime::new().expect("Failed to create Tokio runtime.")
    });
    let rest_base_url = env_var!(REST_BASE_URL default "http://localhost:8081/api/v1/");
    let dao_options = get_dao_options(rest_base_url);

    let result = rt.block_on(async {
      dao_options.init().await
    });

    tracing::info!("database loader init successfully");
    return DBLoader { dao: result.unwrap() };
  }

}

fn get_dao_options(rest_base_url: String) -> DataPackDAOOptions {
  let redis_option = RedisOptions {
    username: env_var!(REDIS_USERNAME),
    host: env_var!(REDIS_PASSWORD default "127.0.0.1"),
    password: Some(env_var!(REDIS_HOST default "apitable@com")),
    port: env_var!(REDIS_PORT)
        .map(|port| port.parse().expect_with(|_| format!("invalid REDIS_PORT: \"{port}\"")))
        .unwrap_or(6379),
    database: Some(0)
  };
  let mysql_option = crate::MysqlOptions {
    username: env_var!(MYSQL_USERNAME default "root"),
    password: env_var!(MYSQL_PASSWORD default "apitable@com"),
    host: env_var!(MYSQL_HOST default "localhost"),
    port: env_var!(MYSQL_PORT)
        .map(|port| port.parse().expect_with(|_| format!("invalid MYSQL_PORT: \"{port}\"")))
        .unwrap_or(3306),
    database: env_var!(MYSQL_DATABASE default "apitable"),
  };
  let dao_options = DataPackDAOOptions {
    redis: redis_option,
    mysql: mysql_option,
    rest_api_base_url: rest_base_url,
    oss_host: env_var!(OSS_HOST default ""),
    table_prefix: env_var!(DATABASE_TABLE_PREFIX default "apitable_"),
  };

  dao_options
}

#[async_trait]
impl IDatasheetPackLoader for DBLoader {
  async fn get_datasheet_pack(&self, datasheet_id: &str) -> anyhow::Result<DatasheetPack> {
    self
      .dao
      .fetch_datasheet_pack(
        "datasheet",
        datasheet_id,
        AuthHeader {
          internal: Some(true),
          ..Default::default()
        },
        FetchDataPackOrigin {
          internal: true,
          main: Some(true),
          ..Default::default()
        },
        None,
      )
      .await
  }
}
