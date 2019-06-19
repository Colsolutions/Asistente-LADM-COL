FORMS = ../ui/dlg_load_layers.ui \
        ../ui/settings_dialog.ui \
        ../ui/dlg_quality.ui \
        ../ui/about_dialog.ui \
        ../ui/controlled_measurement_dialog.ui \
        ../ui/upload_progress_dialog.ui \
        ../ui/dlg_group_party.ui \
        ../ui/dlg_log_excel.ui \
        ../ui/dlg_log_quality.ui \
        ../ui/qgis_model_baker/dlg_import_schema.ui \
        ../ui/qgis_model_baker/dlg_import_data.ui \
        ../ui/qgis_model_baker/dlg_export_data.ui \
        ../ui/dockwidget_queries.ui \
        ../ui/wiz_associate_extaddress_cadastre.ui \
        ../ui/wiz_create_points_cadastre.ui \
        ../ui/wiz_create_administrative_source_cadastre.ui \
        ../ui/wiz_create_building_valuation.ui \
        ../ui/wiz_create_building_unit_qualification_valuation.ui \
        ../ui/wiz_create_building_unit_valuation.ui \
        ../ui/wiz_create_common_equipment_valuation.ui \
        ../ui/wiz_create_geoeconomic_zone_valuation.ui \
        ../ui/wiz_create_horizontal_property_valuation.ui \
        ../ui/wiz_create_plot_cadastre.ui \
        ../ui/wiz_create_boundaries_cadastre.ui \
        ../ui/wiz_create_parcel_cadastre.ui \
        ../ui/wiz_create_parcel_valuation.ui \
        ../ui/wiz_create_physical_zone_valuation.ui \
        ../ui/wiz_create_building_cadastre.ui \
        ../ui/wiz_create_right_of_way_cadastre.ui \
        ../ui/wiz_create_col_party_cadastre.ui \
        ../ui/wiz_create_responsibility_cadastre.ui \
        ../ui/wiz_create_restriction_cadastre.ui \
        ../ui/wiz_create_right_cadastre.ui \
        ../ui/wiz_create_spatial_source_cadastre.ui \
        ../ui/wiz_create_legal_party_prc.ui \
        ../ui/wiz_create_market_research_prc.ui \
        ../ui/wiz_create_natural_party_prc.ui \
        ../ui/wiz_create_nuclear_family_prc.ui \
        ../ui/wiz_create_property_record_card_prc.ui \
        ../ui/change_detection/changes_all_parcels_panel_widget.ui \
        ../ui/change_detection/changes_per_parcel_panel_widget.ui \
        ../ui/change_detection/dockwidget_change_detection.ui \
        ../ui/change_detection/parcels_changes_summary_panel_widget.ui \
        ../ui/dockwidget_changes.ui \
        ../ui/official_data_settings_dialog.ui

SOURCES = ../__init__.py \
          ../asistente_ladm_col_plugin.py \
          ../utils/qgis_utils.py \
          ../utils/logic_checks.py \
          ../utils/qt_utils.py \
          ../utils/quality.py \
          ../utils/model_parser.py \
          ../gui/custom_model_dir.py \
          ../gui/dialog_import_from_excel.py \
          ../gui/dlg_get_db_or_schema_name.py \
          ../gui/dlg_get_java_path.py \
          ../gui/associate_extaddress_cadastre_wizard.py \
          ../gui/create_administrative_source_cadastre_wizard.py \
          ../gui/create_building_unit_qualification_valuation_wizard.py \
          ../gui/create_building_unit_valuation_wizard.py \
          ../gui/create_building_valuation_wizard.py \
          ../gui/create_col_party_cadastre_wizard.py \
          ../gui/create_common_equipment_valuation_wizard.py \
          ../gui/create_geoeconomic_zone_valuation_wizard.py \
          ../gui/create_group_party_cadastre.py \
          ../gui/create_horizontal_property_valuation_wizard.py \
          ../gui/create_responsibility_cadastre_wizard.py \
          ../gui/create_restriction_cadastre_wizard.py \
          ../gui/create_right_cadastre_wizard.py \
          ../gui/create_spatial_source_cadastre_wizard.py \
          ../gui/dialog_load_layers.py \
          ../gui/create_plot_cadastre_wizard.py \
          ../gui/create_boundaries_cadastre_wizard.py \
          ../gui/create_points_cadastre_wizard.py \
          ../gui/create_parcel_cadastre_wizard.py \
          ../gui/create_building_cadastre_wizard.py \
          ../gui/create_building_unit_cadastre_wizard.py \
          ../gui/create_right_of_way_cadastre_wizard.py \
          ../gui/create_legal_party_prc.py \
          ../gui/create_market_research_prc.py \
          ../gui/create_natural_party_prc.py \
          ../gui/create_nuclear_family_prc.py \
          ../gui/create_parcel_valuation_wizard.py \
          ../gui/create_physical_zone_valuation_wizard.py \
          ../gui/create_property_record_card_prc.py \
          ../gui/dockwidget_queries.py \
          ../gui/about_dialog.py \
          ../gui/settings_dialog.py \
          ../gui/dialog_quality.py \
          ../gui/toolbar.py \
          ../gui/right_of_way.py \
          ../gui/reports.py \
          ../gui/controlled_measurement_dialog.py \
          ../gui/upload_progress_dialog.py \
          ../gui/log_quality_dialog.py \
          ../gui/log_excel_dialog.py \
          ../gui/qgis_model_baker/dlg_import_schema.py \
          ../gui/qgis_model_baker/dlg_import_data.py \
          ../gui/qgis_model_baker/dlg_export_data.py \
          ../lib/dbconnector/gpkg_connector.py \
          ../lib/dbconnector/pg_connector.py \
          ../lib/source_handler.py \
          ../config/general_config.py \
          ../config/help_strings.py \
          ../data/ladm_data.py \
          ../gui/official_data_settings_dialog.py \
          ../gui/change_detection/changes_all_parcels_panel.py \
          ../gui/change_detection/changes_per_parcel_panel.py \
          ../gui/change_detection/dockwidget_change_detection.py \
          ../gui/change_detection/parcels_changes_summary_panel.py

TRANSLATIONS = Asistente-LADM_COL_es.ts
