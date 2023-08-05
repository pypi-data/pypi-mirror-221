use std::sync::Arc;

use databus_dao_db::DBLoader;
use databus_core::DataFunctionsManager;
use pyo3::prelude::*;


use pyo3::wrap_pyfunction;
use tokio::runtime::Runtime;

use pyo3::sync::GILOnceCell;

static ASYNC_TOKIO_RUNTIME: GILOnceCell<Runtime> = GILOnceCell::new();


#[pyfunction]
pub fn init(py: Python<'_>, rest_base_url: String) -> PyResult<bool> {
    let rt = ASYNC_TOKIO_RUNTIME.get_or_init(py, || {
        Runtime::new().expect("Failed to create Tokio runtime for databus-core.")
    });
    rt.block_on(async {
        let loader = Arc::new(DBLoader::ainit().await);
        DataFunctionsManager::init(rest_base_url, loader.clone()).await;
        databus_core::init(true, "".to_string(), loader.clone()).await;
        println!("databus-core init done.");
    });
    println!("databus-python init done.");
    Ok(true)
}

/**
 * Return datasheet pack Dict
 */
#[pyfunction]
pub fn get_datasheet_pack(py: Python<'_>, dst_id: String) -> PyResult<String> {
    let pack = ASYNC_TOKIO_RUNTIME.get(py).unwrap().block_on(async {
        let manager = DataFunctionsManager::get_instance();
        let pack = manager.get_datasheet_pack(&dst_id).await.unwrap();
        pack
    });
    Ok(serde_json::to_string(&pack).unwrap())
}


/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}



/// A Python module implemented in Rust.
#[pymodule]
fn databus(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(init, m)?)?;
    m.add_function(wrap_pyfunction!(get_datasheet_pack, m)?)?;

    // get_datasheet_pack -> DatasheetPack
    // get_records(datasheet_id, view_id) -> GetResult<Vec<Record>, DatasheetPack>
    // add_records(datasheet_id, view_id, new_record) -> updated DatasheetPack
    // update_records(datasheet_id, view_id, record_id, update_record) -> updated DatasheetPack
    // delete_records(datasheet_id, view_id, record_id) -> updated DatasheetPack
    // get_views(datasheet_id)

    // m.add_class::<DataBus>()?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use pyo3::prelude::*;

    // #[tokio::test(flavor = "multi_thread", worker_threads = 1)]
    // async fn test_get_data_pack_async() {
    //   let loader = Arc::new(DBLoader::ainit().await);
    //   let init_result = databus_core::init(true, "TODO".to_string(), loader).await;
    //   assert!(init_result);
    //   let manager = DataFunctionsManager::get_instance();
    //   let dst_id = "dstjL5eP37l5vY8ERJ";
    //   let _pack = manager.get_datasheet_pack(dst_id).await.expect("Failed to get datasheet pack.");
    //   assert_eq!(_pack.datasheet.id, dst_id);
    // }

}