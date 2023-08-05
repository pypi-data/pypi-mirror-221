use super::NodeInfo;
use super::UnitInfo;
use super::{DatasheetMeta, Field};
use crate::types::{HashMap, Json};
use crate::shared::JsonExt;
use serde::{Deserialize, Serialize};

use async_trait::async_trait;

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct DatasheetPack {
  pub snapshot: DatasheetSnapshot,
  pub datasheet: NodeInfo,

  #[serde(skip_serializing_if = "JsonExt::is_falsy")]
  pub field_permission_map: Option<Json>,

  #[serde(skip_serializing_if = "Option::is_none")]
  pub foreign_datasheet_map: Option<HashMap<String, BaseDatasheetPack>>,

  #[serde(skip_serializing_if = "Vec::is_empty")]
  pub units: Vec<UnitInfo>,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct DatasheetSnapshot {
  pub meta: DatasheetMeta,
  pub record_map: RecordMap,
  pub datasheet_id: String,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct BaseDatasheetPack {
  pub snapshot: DatasheetSnapshot,
  pub datasheet: Json,

  #[serde(skip_serializing_if = "JsonExt::is_falsy")]
  pub field_permission_map: Option<Json>,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct Record {
  pub id: String,
  pub comment_count: u32,
  pub data: Json,
  pub created_at: i64,
  pub updated_at: Option<i64>,
  pub revision_history: Option<Vec<u32>>,
  pub record_meta: Option<Json>,
}

pub type RecordMap = HashMap<String, Record>;

pub type FieldMap = HashMap<String, Field>;

/**
 * DAO(Data Access Objects) Manager
 *
 * DAO is a class that provides an abstract interface to some type of database or other persistence mechanism.
 * All DB(MySQL, PostgreSQL, MongoDB, etc.) operations should be implemented in DAOs.
 *
 * For example,  
 * `ChangesetsDAO` is a DAO for `changesets` table.
 * `Changeset` is a PO(persistent object) for `changesets` table.
 *  Space, Datasheet, Views are all BOs (Business Objects).
 */
pub trait BaseDAO {}

pub trait BasePO {}

#[async_trait]
/**
 * Snapshot Loader
 */
pub trait IDatasheetPackLoader: Send + Sync {
  // fn init(&mut self, rest_base_url: String) -> bool;
  async fn get_datasheet_pack(&self, datasheet_id: &str) -> anyhow::Result<DatasheetPack>;
}
