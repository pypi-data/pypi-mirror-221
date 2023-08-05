use super::space::Space;
use std::collections::HashMap;

pub struct DataObjectsManager {}

impl DataObjectsManager {
  pub fn new() -> DataObjectsManager {
    return DataObjectsManager {};
  }

  /**
   * Get a real-time collaboration database space instance with space_id
   */
  pub fn get_space(&self, space_id: &str) -> Space {
    return Space {
      space_id: space_id.to_string(),
      datasheets: HashMap::new(),
    };
  }
}
