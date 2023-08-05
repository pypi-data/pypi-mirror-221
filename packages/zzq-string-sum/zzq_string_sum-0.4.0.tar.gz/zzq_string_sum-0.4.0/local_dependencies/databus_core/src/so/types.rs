use std::collections::HashMap;

use serde::{Deserialize, Serialize};
use serde_json::Value;

/**
 * Snapshot is the basic data OT data structure tho hold the data includes:
 * - Datasheet Views
 * - Views Records
 * - Records Rows
 */
#[derive(Serialize, Deserialize)]
pub struct Snapshot {
  pub meta: Meta,

  #[serde(rename = "recordMap")]
  pub record_map: HashMap<String, Record>,

  #[serde(rename = "datasheetId")]
  pub datasheet_id: Option<String>,
  // pub foreignDatasheetMap: HashMap<String, Snapshot>,
}

impl Snapshot {
  /**
   * Make a JSON string in to a snapshot
   */
  pub fn deserialize(snapshot_json: &str) -> Self {
    let snapshot: Snapshot = serde_json::from_str(snapshot_json).unwrap();
    return snapshot;
  }

  pub fn new(datasheet_id: &str) -> Self {
    let record_map: HashMap<String, Record> = HashMap::new();

    return Self {
      meta: Meta::new(),
      record_map: record_map,
      datasheet_id: Some(datasheet_id.to_string()),
    };
  }

  pub fn get_records(&self) -> Vec<&Record> {
    let mut records: Vec<&Record> = Vec::new();
    for (_, record) in &self.record_map {
      records.push(record);
    }
    return records;
  }
}

#[derive(Serialize, Deserialize)]
pub struct Record {
  id: String,
  data: HashMap<String, Value>, // json value

  #[serde(rename = "createdAt")]
  created_at: u64,

  #[serde(rename = "updatedAt")]
  updated_at: u64,
}

impl Record {
  pub fn new() -> Self {
    return Record {
      // snapshot: snapshot,
      id: "".to_string(),
      data: HashMap::new(),
      created_at: 0,
      updated_at: 0,
    };
  }

  pub fn get_primary_field_id(&self) -> String {
    return "".to_string();
  }
}

#[derive(Serialize, Deserialize)]
pub struct Meta {
  views: Vec<ViewProperty>,
  #[serde(rename = "fieldMap")]
  field_map: HashMap<String, Field>,
  // widgetPanel: Vec<Value>, // json value
}
impl Meta {
  fn new() -> Self {
    return Self {
      field_map: HashMap::new(),
      views: Vec::new(),
    };
  }
}

#[derive(Serialize, Deserialize)]
pub struct Field {
  id: String,
  name: String,
  r#type: u64,
}

#[derive(Serialize, Deserialize)]
pub struct ViewProperty {
  id: String,
  name: String,
  r#type: u64,
  columns: Vec<ViewColumn>,
  // Rows
  // GroupInfo
  // FilterInfo
}

#[derive(Serialize, Deserialize)]
pub struct ViewColumn {
  #[serde(rename = "fieldId")]
  field_id: String,
}
