use super::datasheet::Datasheet;
use super::types::BaseBO;

use std::collections::HashMap;

pub struct Space {
  pub space_id: String,
  pub datasheets: HashMap<String, Datasheet>,
}
impl BaseBO for Space {}
impl Space {
  pub fn get_datasheet(&self, datasheet_id: &str) -> &Datasheet {
    return &self.datasheets[datasheet_id];
  }
}
