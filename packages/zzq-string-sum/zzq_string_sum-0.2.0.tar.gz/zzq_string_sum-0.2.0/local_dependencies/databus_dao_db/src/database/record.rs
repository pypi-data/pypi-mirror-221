use super::record_comment::DatasheetRecordCommentDAO;
use crate::DBManager;
use anyhow::Context;
use async_trait::async_trait;
use databus_core::types::HashMap;
use databus_core::types::Json;
use databus_core::types::{Record, RecordMap};
use databus_core::{fix_json, OptionBoolExt, SqlExt};
use futures::TryStreamExt;
use mysql_async::{Params, Value};
use std::sync::Arc;
use time::PrimitiveDateTime;

#[async_trait]
pub trait DatasheetRecordDAO: Send + Sync {
  async fn get_records(
    &self,
    dst_id: &str,
    record_ids: Option<Vec<String>>,
    is_deleted: bool,
    with_comment: bool,
  ) -> anyhow::Result<RecordMap>;
}

struct DatasheetRecordDAOImpl {
  repo: Arc<dyn DBManager>,
  record_comment_dao: Arc<dyn DatasheetRecordCommentDAO>,
}

pub fn new_dao(
  repo: Arc<dyn DBManager>,
  record_comment_dao: Arc<dyn DatasheetRecordCommentDAO>,
) -> Arc<dyn DatasheetRecordDAO> {
  Arc::new(DatasheetRecordDAOImpl {
    repo,
    record_comment_dao: record_comment_dao,
  })
}

#[async_trait]
impl DatasheetRecordDAO for DatasheetRecordDAOImpl {
  async fn get_records(
    &self,
    dst_id: &str,
    record_ids: Option<Vec<String>>,
    is_deleted: bool,
    with_comment: bool,
  ) -> anyhow::Result<RecordMap> {
    if record_ids.as_ref().map(|record_ids| record_ids.is_empty()).is_truthy() {
      return Ok(Default::default());
    }

    let mut query = format!(
      "\
        SELECT `record_id`, `data`, `revision_history`, `field_updated_info`, `created_at`, `updated_at` \
        FROM `{prefix}datasheet_record` \
        WHERE `dst_id` = ? AND `is_deleted` = ?\
      ",
      prefix = self.repo.table_prefix()
    );
    if let Some(record_ids) = &record_ids {
      query.push_str(" AND `record_id`");
      query = query.append_in_condition(record_ids.len());
    }
    let mut client = self.repo.get_client().await?;
    let comment_counts = if with_comment {
      self
        .record_comment_dao
        .get_record_comment_map_by_dst_id(dst_id)
        .await
        .with_context(|| format!("get record comment counts of dst id {dst_id} for build record map"))?
    } else {
      HashMap::default()
    };
    let record_map = client
      .query_all(query, {
        let mut values: Vec<Value> = vec![dst_id.into(), is_deleted.into()];
        if let Some(record_ids) = &record_ids {
          values.extend(record_ids.iter().map(Value::from));
        }
        Params::Positional(values)
      })
      .await
      .with_context(|| format!("get records stream by dst id {dst_id}, record id {record_ids:?}"))?
      .map_ok(|row| {
        let (record_id, data, revision_history, record_meta, created_at, updated_at): (
          String,
          Option<Json>,
          Option<String>,
          Option<Json>,
          PrimitiveDateTime,
          Option<PrimitiveDateTime>,
        ) = row;
        let comment_count = comment_counts.get(&record_id).copied().unwrap_or(0) as u32;
        let record = Record {
          id: record_id.clone(),
          data: fix_json(data.unwrap_or_else(|| Json::Object(Default::default()))),
          comment_count,
          created_at: self.repo.utc_timestamp(created_at),
          updated_at: updated_at.map(|d| self.repo.utc_timestamp(d)),
          revision_history: revision_history.map(|s| s.split(',').map(|n| n.parse().unwrap_or(0)).collect()),
          record_meta: record_meta.map(fix_json),
        };
        (record_id, record)
      })
      .try_collect::<RecordMap>()
      .await
      .with_context(|| format!("get records by dst id {dst_id}, record id {record_ids:?}"));
    record_map
  }
}

#[cfg(test)]
pub mod mock {
  use super::*;
  use databus_core::SliceExt;

  #[derive(Default)]
  pub struct MockDatasheetRecordDAOImpl {
    records: HashMap<&'static str, HashMap<String, Record>>,
  }

  impl MockDatasheetRecordDAOImpl {
    pub fn new() -> Self {
      Self::default()
    }

    pub fn with_records(mut self, records: HashMap<&'static str, HashMap<String, Record>>) -> Self {
      self.records = records;
      self
    }

    pub fn build(self) -> Arc<dyn DatasheetRecordDAO> {
      Arc::new(self)
    }
  }

  #[async_trait]
  impl DatasheetRecordDAO for MockDatasheetRecordDAOImpl {
    async fn get_records(
      &self,
      dst_id: &str,
      record_ids: Option<Vec<String>>,
      _is_deleted: bool,
      _with_comment: bool,
    ) -> anyhow::Result<RecordMap> {
      if let Some(record_ids) = record_ids {
        Ok(self.records.get(dst_id).map_or(HashMap::default(), |records| {
          records
            .iter()
            .filter(|(id, _)| record_ids.contains_ref(*id))
            .map(|(id, record)| (id.to_owned(), record.clone()))
            .collect()
        }))
      } else {
        Ok(self.records.get(dst_id).map_or(HashMap::default(), |records| {
          records
            .iter()
            .map(|(id, record)| (id.to_owned(), record.clone()))
            .collect()
        }))
      }
    }
  }
}

#[cfg(test)]
mod tests {
  use super::*;
  use crate::database::record_comment;
  use crate::mock::{mock_rows, MockRepositoryImpl, MockSqlLog};
  use mysql_async::consts::ColumnType;
  use mysql_async::{params, Row};
  use pretty_assertions::assert_eq;
  use serde_json::json;
  use time::OffsetDateTime;
  use tokio_test::assert_ok;

  fn timestamp(n: i64) -> PrimitiveDateTime {
    let d = OffsetDateTime::from_unix_timestamp_nanos(n as i128 * 1_000_000).unwrap();
    PrimitiveDateTime::new(d.date(), d.time())
      .replace_millisecond(d.millisecond())
      .unwrap()
  }

  fn mock_record_query_results(_is_deleted: bool) -> Vec<Row> {
    mock_rows(
      [
        ("record_id", ColumnType::MYSQL_TYPE_VARCHAR),
        ("data", ColumnType::MYSQL_TYPE_JSON),
        ("revision_history", ColumnType::MYSQL_TYPE_VARCHAR),
        ("field_updated_info", ColumnType::MYSQL_TYPE_JSON),
        ("created_at", ColumnType::MYSQL_TYPE_TIMESTAMP),
        ("updated_at", ColumnType::MYSQL_TYPE_TIMESTAMP),
      ],
      [
        [
          "rec1".into(),
          json!({ "fld1": 123 }).into(),
          "0,3,7,8".into(),
          Value::NULL,
          timestamp(1676945874561).into(),
          timestamp(1676945875561).into(),
        ],
        [
          "rec2".into(),
          json!({ "fld1": 889 }).into(),
          "4".into(),
          json!( { "createdAt": 1676945874561f64 } ).into(),
          timestamp(1676945874561).into(),
          timestamp(1676945875562).into(),
        ],
        [
          "rec3".into(),
          Value::NULL,
          Value::NULL,
          Value::NULL,
          timestamp(1676945874561).into(),
          Value::NULL,
        ],
      ],
    )
  }

  const MOCK_RECORD_WITHOUT_RECORD_IDS_QUERY_SQL: &str = "SELECT \
    `record_id`, \
    `data`, \
    `revision_history`, \
    `field_updated_info`, \
    `created_at`, \
    `updated_at` \
    FROM `apitable_datasheet_record` \
    WHERE `dst_id` = ? \
    AND `is_deleted` = ?";

  const MOCK_RECORD_COMMENT_QUERY_SQL: &str = "SELECT \
    `record_id`, \
    COUNT(*) AS `count` \
    FROM `apitable_datasheet_record_comment` \
    WHERE `dst_id` = :dst_id \
    AND `is_deleted` = 0 \
    GROUP BY `record_id`";

  fn mock_dao<I>(results: I) -> (Arc<dyn DBManager>, Arc<dyn DatasheetRecordDAO>)
  where
    I: IntoIterator<Item = Vec<Row>>,
  {
    let repo = MockRepositoryImpl::new(results);
    (repo.clone(), new_dao(repo.clone(), record_comment::new_dao(repo)))
  }

  #[tokio::test]
  async fn get_records_without_record_ids() {
    let (repo, record_dao) = mock_dao([
      mock_rows(
        [
          ("record_id", ColumnType::MYSQL_TYPE_VARCHAR),
          ("count", ColumnType::MYSQL_TYPE_LONG),
        ],
        [["rec1".into(), 2i64.into()], ["rec2".into(), 1i64.into()]],
      ),
      mock_record_query_results(false),
    ]);

    let record_map = assert_ok!(record_dao.get_records("dst1", None, false, true).await);

    assert_eq!(
      record_map,
      [
        (
          "rec1".to_owned(),
          Record {
            id: "rec1".to_owned(),
            comment_count: 2,
            data: json!( { "fld1": 123 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875561),
            revision_history: Some(vec![0, 3, 7, 8]),
            record_meta: None,
          }
        ),
        (
          "rec2".to_owned(),
          Record {
            id: "rec2".to_owned(),
            comment_count: 1,
            data: json!( { "fld1": 889 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875562),
            revision_history: Some(vec![4]),
            record_meta: Some(json! { { "createdAt": 1676945874561f64 }}),
          }
        ),
        (
          "rec3".to_owned(),
          Record {
            id: "rec3".to_owned(),
            comment_count: 0,
            data: json!({}),
            created_at: 1676945874561,
            updated_at: None,
            revision_history: None,
            record_meta: None,
          }
        ),
      ]
      .into_iter()
      .collect::<HashMap<_, _>>()
    );

    assert_eq!(
      repo.take_logs().await,
      [
        MockSqlLog {
          sql: MOCK_RECORD_COMMENT_QUERY_SQL.into(),
          params: params! {
            "dst_id" => "dst1"
          },
        },
        MockSqlLog {
          sql: MOCK_RECORD_WITHOUT_RECORD_IDS_QUERY_SQL.into(),
          params: Params::Positional(vec!["dst1".into(), false.into()])
        },
      ]
    );
  }

  #[tokio::test]
  async fn get_records_with_record_ids() {
    let (repo, record_dao) = mock_dao([vec![], mock_record_query_results(false)]);

    let record_map = assert_ok!(
      record_dao
        .get_records(
          "dst1",
          Some(vec!["rec1".to_owned(), "rec2".to_owned(), "rec3".to_owned(),]),
          false,
          true
        )
        .await
    );

    assert_eq!(
      record_map,
      [
        (
          "rec1".to_owned(),
          Record {
            id: "rec1".to_owned(),
            comment_count: 0,
            data: json!( { "fld1": 123 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875561),
            revision_history: Some(vec![0, 3, 7, 8]),
            record_meta: None,
          }
        ),
        (
          "rec2".to_owned(),
          Record {
            id: "rec2".to_owned(),
            comment_count: 0,
            data: json!( { "fld1": 889 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875562),
            revision_history: Some(vec![4]),
            record_meta: Some(json! { { "createdAt": 1676945874561f64 }}),
          }
        ),
        (
          "rec3".to_owned(),
          Record {
            id: "rec3".to_owned(),
            comment_count: 0,
            data: json!({}),
            created_at: 1676945874561,
            updated_at: None,
            revision_history: None,
            record_meta: None,
          }
        ),
      ]
      .into_iter()
      .collect::<HashMap<_, _>>()
    );

    assert_eq!(
      repo.take_logs().await,
      [
        MockSqlLog {
          sql: MOCK_RECORD_COMMENT_QUERY_SQL.into(),
          params: params! {
            "dst_id" => "dst1",
          },
        },
        MockSqlLog {
          sql: "SELECT `record_id`, \
        `data`, \
        `revision_history`, \
        `field_updated_info`, \
        `created_at`, \
        `updated_at` \
        FROM `apitable_datasheet_record` \
        WHERE `dst_id` = ? \
        AND `is_deleted` = ? \
        AND `record_id` IN (?,?,?)"
            .into(),
          params: Params::Positional(vec![
            "dst1".into(),
            false.into(),
            "rec1".into(),
            "rec2".into(),
            "rec3".into()
          ])
        },
      ]
    );
  }

  #[tokio::test]
  async fn get_records_deleted() {
    let (repo, record_dao) = mock_dao([vec![], mock_record_query_results(true)]);

    let record_map = assert_ok!(record_dao.get_records("dst1", None, true, true).await);

    assert_eq!(
      record_map,
      [
        (
          "rec1".to_owned(),
          Record {
            id: "rec1".to_owned(),
            comment_count: 0,
            data: json!( { "fld1": 123 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875561),
            revision_history: Some(vec![0, 3, 7, 8]),
            record_meta: None,
          }
        ),
        (
          "rec2".to_owned(),
          Record {
            id: "rec2".to_owned(),
            comment_count: 0,
            data: json!( { "fld1": 889 } ),
            created_at: 1676945874561,
            updated_at: Some(1676945875562),
            revision_history: Some(vec![4]),
            record_meta: Some(json! { { "createdAt": 1676945874561f64 }}),
          }
        ),
        (
          "rec3".to_owned(),
          Record {
            id: "rec3".to_owned(),
            comment_count: 0,
            data: json!({}),
            created_at: 1676945874561,
            updated_at: None,
            revision_history: None,
            record_meta: None,
          }
        ),
      ]
      .into_iter()
      .collect::<HashMap<_, _>>()
    );

    assert_eq!(
      repo.take_logs().await,
      [
        MockSqlLog {
          sql: MOCK_RECORD_COMMENT_QUERY_SQL.into(),
          params: params! {
            "dst_id" => "dst1"
          },
        },
        MockSqlLog {
          sql: MOCK_RECORD_WITHOUT_RECORD_IDS_QUERY_SQL.into(),
          params: Params::Positional(vec!["dst1".into(), true.into()])
        },
      ]
    );
  }
}
