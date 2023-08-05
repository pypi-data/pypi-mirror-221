// migrate from the origin `command manager`

use crate::types::DatasheetPack;

#[allow(dead_code)]
pub enum CommandManager {
  AddFields,
  AddRecords,
  SetRecords,
  SetFieldAttr,
  PasteSetFields,
  PasteSetRecords,
  MoveViews,
  ModifyViews,
  DeleteViews,
  AddViews,
  MoveRow,
  DeleteRecords,
  MoveColumn,
  DeleteField,
  SetSortInfo,
  SetRowHeight,
  SetAutoHeadHeight,
  SetColumnsProperty,
  SetViewFilter,
  SetViewLockInfo,
  SetViewFrozenColumnCount,
  SetGroup,
  SetGalleryStyle,
  SetGanttStyle,
  SetOrgChartStyle,
  SetCalendarStyle,
  FillDataToCells,
  FixConsistency,
  SystemSetRecords,
  SystemSetFieldAttr,
  SetKanbanStyle,
  InsertComment,
  UpdateComment,
  DeleteComment,
  SystemCorrectComment,
  Rollback,
  AddWidgetPanel,
  MoveWidgetPanel,
  ModifyWidgetPanelName,
  DeleteWidgetPanel,
  AddWidgetToPanel,
  DeleteWidget,
  ChangeWidgetInPanelHeight,
  MoveWidget,
  SetGlobalStorage,
  SetWidgetName,
  AddWidgetToDashboard,
  ChangeDashboardLayout,
  DeleteDashboardWidget,
  SetWidgetDepDstId,
  UpdateFormProps,
  SetDateTimeCellAlarm,
  ManualSaveView,
  SetViewAutoSave,
  FixOneWayLinkDstId,
  ResetRecords,
}

pub struct DoCommandResult {}

#[allow(dead_code)]
impl CommandManager {
  pub fn do_command(_datasheet_pack: &DatasheetPack, _command_type: CommandManager) -> DoCommandResult {
    todo!();
  }

  pub fn add_fields() -> Self {
    // TODO: Implement add_fields() function
    Self::AddFields
  }

  pub fn add_records() -> Self {
    // TODO: Implement add_records() function
    Self::AddRecords
  }

  pub fn set_records() -> Self {
    // TODO: Implement set_records() function
    Self::SetRecords
  }

  pub fn set_field_attr() -> Self {
    // TODO: Implement set_field_attr() function
    Self::SetFieldAttr
  }

  pub fn paste_set_fields() -> Self {
    // TODO: Implement paste_set_fields() function
    Self::PasteSetFields
  }

  pub fn paste_set_records() -> Self {
    // TODO: Implement paste_set_records() function
    Self::PasteSetRecords
  }

  pub fn move_views() -> Self {
    // TODO: Implement move_views() function
    Self::MoveViews
  }

  pub fn modify_views() -> Self {
    // TODO: Implement modify_views() function
    Self::ModifyViews
  }

  pub fn delete_views() -> Self {
    // TODO: Implement delete_views() function
    Self::DeleteViews
  }

  pub fn add_views() -> Self {
    // TODO: Implement add_views() function
    Self::AddViews
  }

  pub fn move_row() -> Self {
    // TODO: Implement move_row() function
    Self::MoveRow
  }

  pub fn delete_records() -> Self {
    // TODO: Implement delete_records() function
    Self::DeleteRecords
  }

  pub fn move_column() -> Self {
    // TODO: Implement move_column() function
    Self::MoveColumn
  }

  pub fn delete_field() -> Self {
    // TODO: Implement delete_field() function
    Self::DeleteField
  }

  pub fn set_sort_info() -> Self {
    // TODO: Implement set_sort_info() function
    Self::SetSortInfo
  }

  pub fn set_row_height() -> Self {
    // TODO: Implement set_row_height() function
    Self::SetRowHeight
  }

  pub fn set_auto_head_height() -> Self {
    // TODO: Implement set_auto_head_height() function
    Self::SetAutoHeadHeight
  }

  pub fn set_columns_property() -> Self {
    // TODO: Implement set_columns_property() function
    Self::SetColumnsProperty
  }

  pub fn set_view_filter() -> Self {
    // TODO: Implement set_view_filter() function
    Self::SetViewFilter
  }

  pub fn set_view_lock_info() -> Self {
    // TODO: Implement set_view_lock_info() function
    Self::SetViewLockInfo
  }

  pub fn set_view_frozen_column_count() -> Self {
    // TODO: Implement set_view_frozen_column_count() function
    Self::SetViewFrozenColumnCount
  }

  pub fn set_group() -> Self {
    // TODO: Implement set_group() function
    Self::SetGroup
  }

  pub fn set_gallery_style() -> Self {
    // TODO: Implement set_gallery_style() function
    Self::SetGalleryStyle
  }

  pub fn set_gantt_style() -> Self {
    // TODO: Implement set_gantt_style() function
    Self::SetGanttStyle
  }

  pub fn set_org_chart_style() -> Self {
    // TODO: Implement set_org_chart_style() function
    Self::SetOrgChartStyle
  }

  pub fn set_calendar_style() -> Self {
    // TODO: Implement set_calendar_style() function
    Self::SetCalendarStyle
  }

  pub fn fill_data_to_cells() -> Self {
    // TODO: Implement fill_data_to_cells() function
    Self::FillDataToCells
  }

  pub fn fix_consistency() -> Self {
    // TODO: Implement fix_consistency() function
    Self::FixConsistency
  }

  pub fn system_set_records() -> Self {
    // TODO: Implement system_set_records() function
    Self::SystemSetRecords
  }

  pub fn system_set_field_attr() -> Self {
    // TODO: Implement system_set_field_attr() function
    Self::SystemSetFieldAttr
  }

  pub fn set_kanban_style() -> Self {
    // TODO: Implement set_kanban_style() function
    Self::SetKanbanStyle
  }

  pub fn insert_comment() -> Self {
    // TODO: Implement insert_comment() function
    Self::InsertComment
  }

  pub fn update_comment() -> Self {
    // TODO: Implement update_comment() function
    Self::UpdateComment
  }

  pub fn delete_comment() -> Self {
    // TODO: Implement delete_comment() function
    Self::DeleteComment
  }

  pub fn system_correct_comment() -> Self {
    // TODO: Implement system_correct_comment() function
    Self::SystemCorrectComment
  }

  pub fn rollback() -> Self {
    // TODO: Implement rollback() function
    Self::Rollback
  }

  pub fn add_widget_panel() -> Self {
    // TODO: Implement add_widget_panel() function
    Self::AddWidgetPanel
  }

  pub fn move_widget_panel() -> Self {
    // TODO: Implement move_widget_panel() function
    Self::MoveWidgetPanel
  }

  pub fn modify_widget_panel_name() -> Self {
    // TODO: Implement modify_widget_panel_name() function
    Self::ModifyWidgetPanelName
  }

  pub fn delete_widget_panel() -> Self {
    // TODO: Implement delete_widget_panel() function
    Self::DeleteWidgetPanel
  }

  pub fn add_widget_to_panel() -> Self {
    // TODO: Implement add_widget_to_panel() function
    Self::AddWidgetToPanel
  }

  pub fn delete_widget() -> Self {
    // TODO: Implement delete_widget() function
    Self::DeleteWidget
  }

  pub fn change_widget_in_panel_height() -> Self {
    // TODO: Implement change_widget_in_panel_height() function
    Self::ChangeWidgetInPanelHeight
  }

  pub fn move_widget() -> Self {
    // TODO: Implement move_widget() function
    Self::MoveWidget
  }

  pub fn set_global_storage() -> Self {
    // TODO: Implement set_global_storage() function
    Self::SetGlobalStorage
  }

  pub fn set_widget_name() -> Self {
    // TODO: Implement set_widget_name() function
    Self::SetWidgetName
  }

  pub fn add_widget_to_dashboard() -> Self {
    // TODO: Implement add_widget_to_dashboard() function
    Self::AddWidgetToDashboard
  }

  pub fn change_dashboard_layout() -> Self {
    // TODO: Implement change_dashboard_layout() function
    Self::ChangeDashboardLayout
  }

  pub fn delete_dashboard_widget() -> Self {
    // TODO: Implement delete_dashboard_widget() function
    Self::DeleteDashboardWidget
  }

  pub fn set_widget_dep_dst_id() -> Self {
    // TODO: Implement set_widget_dep_dst_id() function
    Self::SetWidgetDepDstId
  }

  pub fn update_form_props() -> Self {
    // TODO: Implement update_form_props() function
    Self::UpdateFormProps
  }

  pub fn set_date_time_cell_alarm() -> Self {
    // TODO: Implement set_date_time_cell_alarm() function
    Self::SetDateTimeCellAlarm
  }

  pub fn manual_save_view() -> Self {
    // TODO: Implement manual_save_view() function
    Self::ManualSaveView
  }

  pub fn set_view_auto_save() -> Self {
    // TODO: Implement set_view_auto_save() function
    Self::SetViewAutoSave
  }

  pub fn fix_one_way_link_dst_id() -> Self {
    // TODO: Implement fix_one_way_link_dst_id() function
    Self::FixOneWayLinkDstId
  }

  pub fn reset_records() -> Self {
    // TODO: Implement reset_records() function
    Self::ResetRecords
  }
}
