

#![recursion_limit = "256"]
use std::sync::Arc;

///
/// 这里lib的主入口，涉及到对外暴露的接口，请不要随意暴露接口，要得到大家的评审确认，避免对外接口爆炸和凌乱。
/// This is the main entry point of the lib, involving the exposed interfaces.
/// Please do not expose interfaces arbitrarily, and obtain the approval of everyone to avoid interface explosion and disorder.
///
/// Author: Kelly Peilin Chan <kelly@apitable.com>
///
// TODO, refactor types2.rs
// use types::*;

/// Will be private in the future.
// pub mod services;
// pub mod tablebundle;
mod bo;
pub use bo::DataObjectsManager;

/// Will be private in the future.
pub mod so;

pub mod types;

#[macro_use]
pub mod shared;
pub use shared::*;
// #[macro_use]
// extern crate napi_derive;
#[cfg(test)]
use rstest_reuse;

/**
 * DataBundleManager, bindings functions all here.
 */
pub use so::DataFunctionsManager;

use shared::logging;
use types::IDatasheetPackLoader;
// mod bo;
// pub use bo::space::Space;

// Unit models
// #[macro_use]
// pub mod dao;

mod ot;

// #[macro_use]
// extern crate databus_core;

// #[macro_use]
// extern crate napi_derive;

/**
 * Initialize function
 */
pub async fn init(is_dev_mode: bool, rest_base_url: String, loader: Arc<dyn IDatasheetPackLoader>) -> bool {
  logging::init(is_dev_mode);
  DataFunctionsManager::init(rest_base_url, loader).await;
  println!("databus-core init done and return");
  return true;
}
