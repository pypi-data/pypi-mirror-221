use super::types::BaseBO;

pub struct Datasheet {}

impl Datasheet {

  fn get_records() -> Record {
    return Record {};
  }

  fn get_fields() -> Field {
    return Field {};
  }
}
impl BaseBO for Datasheet {}
pub struct Field {}

pub struct Record {}
impl BaseBO for Record {}

pub struct View {}

impl BaseBO for View {}
