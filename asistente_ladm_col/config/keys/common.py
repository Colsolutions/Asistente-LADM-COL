from asistente_ladm_col.config.ladm_names import LADMNames

DEFAULT_GUI = 'DEFAULT_GUI'
TEMPLATE_GUI = 'TEMPLATE_GUI'

ACTION = 'action'
DEFAULT_ACTION_TEXT = 'default_action_text'
DEFAULT_ACTION_STATUS = 'default_action_status'
OBJECT_NAME = 'object_name'
ICON = 'icon'
ACTIONS = 'actions'
MAIN_MENU = 'main_menu'
WIDGET_NAME = 'widget_name'
MENU = 'menu'
TOOLBAR = 'toolbar'
WIDGET_TYPE = 'widget_type'
SEPARATOR = 'separator'
NO_MENU = 'no_menu'
OPERATION_MENU = 'operation_menu'
SUPPLIES_MENU = 'supplies_menu'
LADM_COL_ADD_ON_MENU = 'ladm_col_add_on_menu'

ROLE_ACTIONS = 'role_actions'
ROLE_NAME = 'role_name'
ROLE_ENABLED = 'role_enabled'
ROLE_DESCRIPTION = 'role_description'
ROLE_GUI_CONFIG = 'role_gui_config'
ROLE_MODELS = 'role_models'
ROLE_DB_SOURCE = 'role_db_source'
ROLE_MODEL_ILI2DB_PARAMETERS = 'role_model_ili2db_parameters'
ROLE_QUALITY_RULES = 'rule_quality_rules'
ROLE_NEEDS_AUTOMATIC_VALUE_FOR_BASKETS = 'role_needs_automatic_value_for_baskets'
BASIC_ROLE = 'basic_role'
SUPPLIES_PROVIDER_ROLE = 'supplies_provider_role'
FIELD_ADMIN_ROLE = 'field_admin_role'
FIELD_COORDINATOR_ROLE = 'field_coordinator_role'
OPERATOR_ROLE = 'operator_role'
MANAGER_ROLE = 'manager_role'
ADVANCED_ROLE = 'advanced_role'
ADMINISTRATOR_ROLE = 'administrator_role'

REQUIRED_MODELS = "required_models"
ROLE_SUPPORTED_MODELS = "role_supported_models"
ROLE_HIDDEN_MODELS = "role_hidden_models"
ROLE_CHECKED_MODELS = "role_checked_models"
COMMON_SUPPORTED_MODELS = [LADMNames.LADM_COL_MODEL_KEY,
                           LADMNames.ISO19107_MODEL_KEY,
                           LADMNames.SURVEY_MODEL_KEY,
                           LADMNames.SUPPLIES_MODEL_KEY,
                           LADMNames.SNR_DATA_SUPPLIES_MODEL_KEY,
                           LADMNames.SUPPLIES_INTEGRATION_MODEL_KEY,
                           LADMNames.CADASTRAL_CARTOGRAPHY_MODEL_KEY,
                           LADMNames.VALUATION_MODEL_KEY,
                           LADMNames.CATALOG_OBJECTS_MODEL_KEY,
                           LADMNames.QUALITY_ERROR_MODEL_KEY]
COMMON_HIDDEN_MODELS = [LADMNames.LADM_COL_MODEL_KEY,
                        LADMNames.ISO19107_MODEL_KEY,
                        LADMNames.CATALOG_OBJECTS_MODEL_KEY]
COMMON_CHECKED_MODELS = [LADMNames.SURVEY_MODEL_KEY]
COMMON_ROLE_MODELS = {ROLE_SUPPORTED_MODELS: COMMON_SUPPORTED_MODELS,
                      ROLE_HIDDEN_MODELS: COMMON_HIDDEN_MODELS,
                      ROLE_CHECKED_MODELS: COMMON_CHECKED_MODELS}

ALL_QUALITY_RULES = "all_quality_rules"

ALL_ROLES = 'all_roles'
ACTION_SETTINGS = 'action_settings'
ACTION_HELP = 'action_help'
ACTION_ABOUT = 'action_about'

ACTION_DOWNLOAD_GUIDE = 'action_download_guide'
ACTION_FINALIZE_GEOMETRY_CREATION = 'action_finalize_geometry_creation'
ACTION_BUILD_BOUNDARY = 'action_build_boundary'
ACTION_MOVE_NODES = 'action_move_nodes'
ACTION_FILL_BFS = 'action_fill_bfs'
ACTION_FILL_MORE_BFS_AND_LESS = 'action_fill_more_bfs_and_less'
ACTION_FILL_RIGHT_OF_WAY_RELATIONS = 'action_fill_right_of_way_relations'
ACTION_IMPORT_FROM_INTERMEDIATE_STRUCTURE = 'action_import_from_intermediate_structure'

ACTION_RUN_ETL_SUPPLIES = 'action_run_etl_supplies'
ACTION_FIND_MISSING_COBOL_SUPPLIES = 'action_find_missing_cobol_supplies'
ACTION_FIND_MISSING_SNC_SUPPLIES = 'action_find_missing_snc_supplies'
ACTION_INTEGRATE_SUPPLIES = 'action_integrate_supplies'

ACTION_ALLOCATE_PARCELS_FIELD_DATA_CAPTURE = 'action_allocate_parcels_field_data_capture'
ACTION_SYNCHRONIZE_FIELD_DATA = 'action_synchronize_field_data'

ACTION_ST_LOGIN = 'action_st_login'
ACTION_ST_LOGOUT = 'action_st_logout'
ACTION_ST_UPLOAD_XTF = 'action_st_upload_xtf'

ACTION_CHECK_QUALITY_RULES = 'action_check_quality_rules'
ACTION_PARCEL_QUERY = 'action_parcel_query'
ACTION_CREATE_BOUNDARY = 'action_create_boundary'
ACTION_CREATE_POINT = 'action_create_point'
ACTION_CREATE_PLOT = 'action_create_plot'
ACTION_CREATE_BUILDING = 'action_create_building'
ACTION_CREATE_BUILDING_UNIT = 'action_create_building_unit'
ACTION_CREATE_RIGHT_OF_WAY = 'action_create_right_of_way'
ACTION_CREATE_EXT_ADDRESS = 'action_create_ext_address'
ACTION_CREATE_PARCEL = 'action_create_parcel'
ACTION_CREATE_PARTY = 'action_create_party'
ACTION_CREATE_GROUP_PARTY = 'action_create_group_party'
ACTION_CREATE_RIGHT = 'action_create_right'
ACTION_CREATE_RESTRICTION = 'action_create_restriction'
ACTION_CREATE_ADMINISTRATIVE_SOURCE = 'action_create_administrative_source'
ACTION_CREATE_SPATIAL_SOURCE = 'action_create_spatial_source'
ACTION_UPLOAD_PENDING_SOURCE = 'action_upload_pending_source'
ACTION_SCHEMA_IMPORT = 'action_schema_import'
ACTION_IMPORT_DATA = 'action_import_data'
ACTION_EXPORT_DATA = 'action_export_data'
ACTION_XTF_MODEL_CONVERTER = 'action_xtf_model_converter'
ACTION_LOAD_LAYERS = 'action_load_layers'
ACTION_FIX_LADM_COL_RELATIONS = 'action_fix_ladm_col_relations'
ACTION_REPORT_ANNEX_17 = 'action_report_annex_17'
ACTION_REPORT_ANT = 'action_report_ant'
ACTION_CHANGE_DETECTION_PER_PARCEL = 'action_change_detection_per_parcel'
ACTION_CHANGE_DETECTION_ALL_PARCELS = 'action_change_detection_all_parcels'
ACTION_CHANGE_DETECTION_SETTINGS = "action_change_detection_settings"

ALL_ACTIONS = 'all_actions'

DOCK_WIDGET_FIELD_DATA_CAPTURE = "dock_widget_field_data_capture"
DOCK_WIDGET_QUERIES = "dock_widget_queries"
DOCK_WIDGET_CHANGE_DETECTION = "dock_widget_change_detection"
DOCK_WIDGET_TRANSITION_SYSTEM = "dock_widget_transition_system"
DOCK_WIDGET_QUALITY_RULES = "dock_widget_quality_rules"

SURVEYING_ICON = ":/Asistente-LADM-COL/resources/images/surveying.png"
DATA_MANAGEMENT_ICON = ":/Asistente-LADM-COL/resources/images/create_db.png"
FIELD_DATA_CAPTURE_ICON = ":/Asistente-LADM-COL/resources/images/process.svg"
DATA_CREATION_ICON = ":/Asistente-LADM-COL/resources/images/data_creation.svg"
ST_ICON = ":/Asistente-LADM-COL/resources/images/st.svg"
OPERATION_ICON = ":/Asistente-LADM-COL/resources/images/icon.png"
STRUCTURING_TOOLS_ICON = ":/Asistente-LADM-COL/resources/images/structuring_tools.svg"
SUPPLIES_ICON = ""
SPATIAL_UNIT_ICON = ":/Asistente-LADM-COL/resources/images/spatial_unit.png"
BA_UNIT_ICON = ":/Asistente-LADM-COL/resources/images/ba_unit.png"
RRR_ICON = ":/Asistente-LADM-COL/resources/images/rrr.png"
PARTY_ICON = ":/Asistente-LADM-COL/resources/images/party.png"
SOURCE_ICON = ":/Asistente-LADM-COL/resources/images/source.png"
REPORTS_ICON = ":/Asistente-LADM-COL/resources/images/reports.svg"
CHANGE_DETECTION_ICON = ":/Asistente-LADM-COL/resources/images/change_detection.svg"
ADD_ON_ICON = ":/Asistente-LADM-COL/resources/images/add_on.png"

# MENU OBJECTNAMES
MENU_SURVEY_OBJECTNAME = "ladm_col_survey_menu"
MENU_LADM_COL_OBJECTNAME = "ladm_col_menu"
MENU_REPORTS_OBJECTNAME = "ladm_col_reports_menu"

# MODEL KEYS
MODEL_ALIAS = "MODEL_ALIAS"
MODEL_IS_SUPPORTED = "MODEL_IS_SUPPORTED"
MODEL_SUPPORTED_VERSION = "MODEL_SUPPORTED_VERSION"
MODEL_HIDDEN_BY_DEFAULT = "MODEL_HIDDEN_BY_DEFAULT"
MODEL_CHECKED_BY_DEFAULT = "MODEL_CHECKED_BY_DEFAULT"
MODEL_ILI2DB_PARAMETERS = "MODEL_ILI2DB_PARAMETERS"
MODEL_MAPPING = "MODEL_MAPPING"
MODEL_DIR = "MODEL_DIR"
MODEL_BASKET_INFO = "MODEL_BASKET_INFO"
MODEL_BASKET_TOPIC_NAME = "MODEL_BASKET_TOPIC_NAME"
MODEL_BASKET_TOPIC_NAME_PREFERRED = "MODEL_BASKET_TOPIC_NAME_PREFERRED"
MODEL_CATALOGS = "MODEL_CATALOGS"

# Nowadays just an example, it is not being used, although initially planned
MODELS_GUI_DICT = {
    LADMNames.SURVEY_MODEL_KEY: [
        ACTION_CHECK_QUALITY_RULES
    ],
    LADMNames.VALUATION_MODEL_KEY: [
    ],
    LADMNames.SUPPLIES_MODEL_KEY: [
        ACTION_RUN_ETL_SUPPLIES,
        ACTION_FIND_MISSING_COBOL_SUPPLIES,
        ACTION_FIND_MISSING_SNC_SUPPLIES,
    ]
}

# QUALITY RULES
QUALITY_RULE_LAYERS = "QUALITY_RULE_LAYERS"
QUALITY_RULE_LADM_COL_LAYERS = "QUALITY_RULE_LADM_COL_LAYERS"
QUALITY_RULE_ADJUSTED_LAYERS = "QUALITY_RULE_ADJUSTED_LAYERS"
HAS_ADJUSTED_LAYERS = "HAS_ADJUSTED_LAYERS"
FIX_ADJUSTED_LAYER = "FIX_ADJUSTED_LAYER"
ADJUSTED_INPUT_LAYER = "ADJUSTED_INPUT_LAYER"
ADJUSTED_REFERENCE_LAYER = "ADJUSTED_REFERENCE_LAYER"
ADJUSTED_BEHAVIOR = "ADJUSTED_BEHAVIOR"
ADJUSTED_TOPOLOGICAL_POINTS = "ADJUSTED_TOPOLOGICAL_POINTS"
