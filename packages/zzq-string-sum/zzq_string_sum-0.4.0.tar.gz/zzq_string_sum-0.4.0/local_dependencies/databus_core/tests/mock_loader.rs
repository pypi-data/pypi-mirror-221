use async_trait::async_trait;
use databus_core::types::{DatasheetPack, IDatasheetPackLoader};
use serde_json::Value;

pub struct MockLoader {
  pub json: String,
}

#[async_trait]
impl IDatasheetPackLoader for MockLoader {
  async fn get_datasheet_pack(&self, _datasheet_id: &str) -> anyhow::Result<DatasheetPack> {
    let response: Value = serde_json::from_str(&self.json)?;
    let data = response.get("data").unwrap();

    serde_json::from_value(data.clone()).map_err(|e| anyhow::anyhow!(e))
  }
}
