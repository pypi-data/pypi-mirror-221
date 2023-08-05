use super::api_mock::MOCK_DATASHEET_PACK_JSON;

/**
 * API Client for WebAssembly
 */
pub struct ApiDAO {}

impl ApiDAO {
  /**
   * the whole datasheetPack Response Body
   */
  pub fn fetch_datasheet_pack(datasheet_id: &str) -> String {
    if datasheet_id == "mock" {
      return MOCK_DATASHEET_PACK_JSON.to_string();
    }

    return MOCK_DATASHEET_PACK_JSON.to_string();
  }
}
