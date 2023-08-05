use std::sync::{Arc, Mutex};

use crate::types::IDatasheetPackLoader;
// use std::sync::{OnceLock, OnceCell, Mutex};
use once_cell::sync::OnceCell;

// use crate::dao::{DataPackDAOOptions, RedisOptions};
use crate::so::types::Record;
use crate::types::DatasheetPack;

use super::data_bundle::DataBundle;

/**
 * DataBundle Manager, the m`ain entry and binding functions' mother.
 */
pub struct DataFunctionsManager {
  /**
   * Shared Singleton DataBundle to store and first-level cache the DatasheetPacks.
   */
  shared_data_bundle: Mutex<DataBundle>,
  datasheet_loader: Arc<dyn IDatasheetPackLoader>,
}

static INSTANCE: OnceCell<DataFunctionsManager> = OnceCell::new();

/**
 * Singleton Shared instance, for future flexible
 */
impl DataFunctionsManager {
  pub async fn init(_rest_base_url: String, datasheet_loader: Arc<dyn IDatasheetPackLoader>) -> bool {
    let _ = INSTANCE.set(DataFunctionsManager {
      shared_data_bundle: Mutex::new(DataBundle::new()),
      datasheet_loader,
    });

    return true;
  }

  pub fn get_instance() -> &'static DataFunctionsManager {
    INSTANCE.get().unwrap()
  }
  // pub fn get_instance_mut() -> &'static mut DataBundleManager {
  //   Self::get_instance();
  //   return unsafe { INSTANCE.get_mut().unwrap() };
  // }

  // pub fn new() -> DataFunctionsManager {
  //   return DataFunctionsManager {
  //     shared_data_bundle: Mutex::new(DataBundle::new()),
  //     datasheet_loader: Mutex::new(SnapshotLoaderType::DBLoader),
  //   };
  // }

  pub async fn get_datasheet_pack(&self, dst_id: &str) -> anyhow::Result<DatasheetPack> {
    let datasheet_pack = self.datasheet_loader
        .get_datasheet_pack(dst_id)
        .await?;
    println!("get_datasheet_pack: {:?}", datasheet_pack);
    self
      .shared_data_bundle
      .lock()
      .unwrap()
      .update(dst_id, datasheet_pack.clone());

    Ok(datasheet_pack)
  }
}

pub async fn get_records() -> Vec<Record> {
  return vec![];
}

pub fn get_fields() {}
pub fn get_views() {}
