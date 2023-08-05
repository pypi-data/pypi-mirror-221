mod loaders;
pub use loaders::*;

pub mod datapack_dao;
pub use datapack_dao::*;

pub mod consts;
pub mod node;
pub mod resource;
mod types;
pub mod unit;
pub mod user;

#[macro_use]
extern crate databus_core;

pub mod db_manager;
pub use db_manager::*;

pub(crate) mod redis;

pub mod database;
pub use database::*;

mod api;
mod rest;
pub use api::*;
mod api_mock;

// #[deprecated(since = "0.0.1", note = "Here is just an example. Remove ASAP.")]

// pub struct UnitsDAO {}

// impl UnitsDAO {
//   pub fn get_units(&self) -> u64 {
//     return 0;
//   }
// }

// impl BaseDAO for UnitsDAO {}
// pub struct Unit {}

// impl BasePO for Unit {}

// pub struct NodeInfo {
//   pub id: String,
//   pub name: String,
//   pub description: String,
// }
// impl BasePO for NodeInfo {}
