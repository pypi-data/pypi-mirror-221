use std::collections::hash_map::Entry;
use std::collections::HashMap;

use crate::types::DatasheetPack;

/**
 * Singleton Shared instance, for future flexible
 */
// static mut SHARED_DATA_BUNDLE: Option<DataBundle> = None; // singleton databundle

/**
 * DataBundle  =   NodeJS IDatasheetMap
 *
 * Memory stores DatasheetPacks.
 * Replacement of frontend's redux.
 *
 * TODO: Auto GC depends on the memory size, size_of<HashMap<K, V>>() + size_of<K>() * capacity + size_of<V>() * capacity
 */
pub struct DataBundle {
  pub datasheet_map: HashMap<String, DatasheetPack>,
}

impl DataBundle {
  pub fn new() -> DataBundle {
    return DataBundle {
      datasheet_map: HashMap::new(),
    };
  }

  /**
   * Return the entry of datasheet map
   */
  fn entry(&mut self, dst_id: &str) -> Entry<'_, std::string::String, DatasheetPack> {
    return self.datasheet_map.entry(dst_id.to_string());
  }

  /**
   * Update the datasheet
   */
  pub fn update(&mut self, dst_id: &str, new_datasheet_pack: DatasheetPack) {
    self.entry(dst_id).or_insert(new_datasheet_pack);
  }

  //   let snapshot = Snapshot::new(dst_id);
  //   let datasheet = NodeInfo {
  //     id: "".to_string(),
  //     name: "".to_string(),
  //     description: "".to_string(),
  //   };
  //   let new_datasheet_pack = DatasheetPack {
  //     id: dst_id.to_string(),
  //     snapshot: snapshot,
  //     datasheet: datasheet,
  //   };
  //   self.datasheet_map.entry(dst_id.to_string()).or_insert(new_datasheet_pack);

  //   return self.datasheet_map.get(dst_id);
  // }
  // pub fn update_datasheet(&self, datasheet_pack: &DatasheetPack) {
  //   self.datasheet_map.insert(datasheet_pack.id.clone(), datasheet_pack);
  // }
}
