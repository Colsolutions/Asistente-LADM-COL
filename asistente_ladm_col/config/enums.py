from enum import (Enum,
                  IntFlag)


class EnumDbActionType(Enum):
    SCHEMA_IMPORT = 1
    IMPORT = 2
    EXPORT = 3
    IMPORT_FROM_ETL = 99
    CONFIG = 100


class EnumTestLevel(IntFlag):
    _CHECK_DB = 2
    _CHECK_SCHEMA = 4
    _CHECK_LADM = 8

    SERVER_OR_FILE = 1
    DB = _CHECK_DB  # 2
    DB_SCHEMA = _CHECK_DB|_CHECK_SCHEMA  # 6
    DB_FILE = _CHECK_DB|_CHECK_SCHEMA  # 6
    LADM = _CHECK_DB|_CHECK_SCHEMA|_CHECK_LADM  # 14
    SCHEMA_IMPORT = 128


class EnumUserLevel(IntFlag):
    CREATE = 1
    CONNECT = 2


class EnumTestConnectionMsg(IntFlag):
    CONNECTION_TO_SERVER_FAILED = 0
    CONNECTION_COULD_NOT_BE_OPEN = 1
    DATABASE_NOT_FOUND = 2
    SCHEMA_NOT_FOUND = 3
    USER_HAS_NO_PERMISSION = 4
    INTERLIS_META_ATTRIBUTES_NOT_FOUND = 5
    INVALID_ILI2DB_VERSION = 6
    NO_LADM_MODELS_FOUND_IN_SUPPORTED_VERSION = 7  # No single model is in the supported version
    REQUIRED_LADM_MODELS_NOT_FOUND = 8  # At least one required model was not found
    DB_NAMES_INCOMPLETE = 9
    UNKNOWN_CONNECTION_ERROR = 10
    DIR_NOT_FOUND = 11
    GPKG_FILE_NOT_FOUND = 12
    WRONG_FILE_EXTENSION = 13
    BASKET_COLUMN_NOT_FOUND = 14

    CONNECTION_OPENED = 100
    CONNECTION_TO_SERVER_SUCCESSFUL = 101
    CONNECTION_TO_DB_SUCCESSFUL = 102
    CONNECTION_TO_SCHEMA_SUCCESSFUL = 103
    DB_WITH_VALID_LADM_COL_STRUCTURE = 104
    SCHEMA_WITH_VALID_LADM_COL_STRUCTURE = 105
    CONNECTION_TO_DB_SUCCESSFUL_NO_LADM_COL = 106
    DB_MODELS_ARE_CORRECT = 107


class EnumWizardType(IntFlag):
    SINGLE_PAGE_WIZARD_TYPE = 1
    SINGLE_PAGE_SPATIAL_WIZARD_TYPE = 2
    MULTI_PAGE_WIZARD_TYPE = 4
    MULTI_PAGE_SPATIAL_WIZARD_TYPE = 8

    SPATIAL_WIZARD = SINGLE_PAGE_SPATIAL_WIZARD_TYPE | MULTI_PAGE_SPATIAL_WIZARD_TYPE
    NON_SPATIAL_WIZARD = SINGLE_PAGE_WIZARD_TYPE | MULTI_PAGE_WIZARD_TYPE


class EnumLogHandler(Enum):
    MESSAGE_BAR = 1
    STATUS_BAR = 2
    QGIS_LOG = 3


class EnumLogMode(Enum):
    USER = 1
    DEV = 2


class EnumLADMQueryType(Enum):
    IGAC_BASIC_INFO = 1
    IGAC_PHYSICAL_INFO = 2
    IGAC_LEGAL_INFO = 3
    IGAC_ECONOMIC_INFO = 4
    IGAC_PROPERTY_RECORD_CARD_INFO = 5


class EnumSpatialOperationType(Enum):
    INTERSECTS = 1
    OVERLAPS = 2
    CONTAINS = 3


class EnumSTTaskStatus(Enum):
    ASSIGNED = "ASIGNADA"
    STARTED = "INICIADA"
    CANCELED = "CANCELADA"
    CLOSED = "CERRADA"


class EnumSTStepType(Enum):
    UPLOAD_FILE = 1
    CONNECT_TO_DB = 2
    SCHEMA_IMPORT = 3
    IMPORT_DATA = 4
    EXPORT_DATA = 5
    RUN_ETL_COBOL = 6


class EnumLayerRegistryType(Enum):
    """
    Loaded layers in QGIS can be: 1) only in registry or 2) both in registry and in layer tree
    """
    ONLY_IN_REGISTRY = 1
    IN_LAYER_TREE = 2


# https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html
class EnumQualityRule:
    class Point(Enum):
        OVERLAPS_IN_BOUNDARY_POINTS = 1001
        OVERLAPS_IN_CONTROL_POINTS = 1002
        BOUNDARY_POINTS_COVERED_BY_BOUNDARY_NODES = 1003
        BOUNDARY_POINTS_COVERED_BY_PLOT_NODES = 1004

    class Line(Enum):
        OVERLAPS_IN_BOUNDARIES = 2001
        BOUNDARIES_ARE_NOT_SPLIT = 2002
        BOUNDARIES_COVERED_BY_PLOTS = 2003
        BOUNDARY_NODES_COVERED_BY_BOUNDARY_POINTS = 2004
        DANGLES_IN_BOUNDARIES = 2005

    class Polygon(Enum):
        OVERLAPS_IN_PLOTS = 3001
        OVERLAPS_IN_BUILDINGS = 3002
        OVERLAPS_IN_RIGHTS_OF_WAY = 3003
        PLOTS_COVERED_BY_BOUNDARIES = 3004
        RIGHT_OF_WAY_OVERLAPS_BUILDINGS = 3005
        GAPS_IN_PLOTS = 3006
        MULTIPART_IN_RIGHT_OF_WAY = 3007
        PLOT_NODES_COVERED_BY_BOUNDARY_POINTS = 3008
        BUILDINGS_SHOULD_BE_WITHIN_PLOTS = 3009
        BUILDING_UNITS_SHOULD_BE_WITHIN_PLOTS = 3010
        BUILDING_UNITS_SHOULD_BE_WITHIN_BUILDINGS = 3011

    class Logic(Enum):
        PARCEL_RIGHT_RELATIONSHIP = 4001
        FRACTION_SUM_FOR_PARTY_GROUPS = 4002
        DEPARTMENT_CODE_HAS_TWO_NUMERICAL_CHARACTERS = 4003
        MUNICIPALITY_CODE_HAS_THREE_NUMERICAL_CHARACTERS = 4004
        PARCEL_NUMBER_HAS_30_NUMERICAL_CHARACTERS = 4005
        PARCEL_NUMBER_BEFORE_HAS_20_NUMERICAL_CHARACTERS = 4006
        COL_PARTY_NATURAL_TYPE = 4007
        COL_PARTY_NOT_NATURAL_TYPE = 4008
        PARCEL_TYPE_AND_22_POSITION_OF_PARCEL_NUMBER = 4009
        UEBAUNIT_PARCEL = 4010
        DUPLICATE_RECORDS_IN_BOUNDARY_POINT = 4011
        DUPLICATE_RECORDS_IN_SURVEY_POINT = 4012
        DUPLICATE_RECORDS_IN_CONTROL_POINT = 4013
        DUPLICATE_RECORDS_IN_BOUNDARY = 4014
        DUPLICATE_RECORDS_IN_PLOT = 4015
        DUPLICATE_RECORDS_IN_BUILDING = 4016
        DUPLICATE_RECORDS_IN_BUILDING_UNIT = 4017
        DUPLICATE_RECORDS_IN_PARCEL = 4018
        DUPLICATE_RECORDS_IN_PARTY = 4019
        DUPLICATE_RECORDS_IN_RIGHT = 4020
        DUPLICATE_RECORDS_IN_RESTRICTION = 4021
        DUPLICATE_RECORDS_IN_ADMINISTRATIVE_SOURCE = 4022


class EnumRelationshipType(Enum):
    # Operations:
    # 1 = One and only one feature must be selected
    # + = One or more features must be selected
    # * = Optional, i.e., zero or more features could be selected
    ONE = 1,
    MANY = 2,
    ONE_OR_MANY = 3


class EnumDigitizedFeatureStatus(Enum):
    INVALID = 1
    ZERO_FEATURES = 2
    OTHER = 3


class EnumRelatableLayers(Enum):
    PLOT = 1
    BUILDING = 2
    BUILDING_UNIT = 3

    BOUNDARY = 4
    BOUNDARY_POINT = 5
    SURVEY_POINT = 6
    CONTROL_POINT = 7

    ADMINISTRATIVE_SOURCE = 8

    @staticmethod
    def enum_value_from_db_name(db_names, item_db_name):
        dict_result = {
            db_names.LC_PLOT_T: EnumRelatableLayers.PLOT,
            db_names.LC_BUILDING_T: EnumRelatableLayers.BUILDING,
            db_names.LC_BUILDING_UNIT_T: EnumRelatableLayers.BUILDING_UNIT,
            db_names.LC_BOUNDARY_T: EnumRelatableLayers.BOUNDARY,
            db_names.LC_BOUNDARY_POINT_T: EnumRelatableLayers.BOUNDARY_POINT,
            db_names.LC_SURVEY_POINT_T: EnumRelatableLayers.SURVEY_POINT,
            db_names.LC_CONTROL_POINT_T: EnumRelatableLayers.CONTROL_POINT,
            db_names.LC_ADMINISTRATIVE_SOURCE_T: EnumRelatableLayers.ADMINISTRATIVE_SOURCE
        }
        return dict_result[item_db_name] if item_db_name in dict_result else None

    def get_db_name(self, db_names):
        dict_result = {
            EnumRelatableLayers.PLOT: db_names.LC_PLOT_T,
            EnumRelatableLayers.BUILDING: db_names.LC_BUILDING_T,
            EnumRelatableLayers.BUILDING_UNIT: db_names.LC_BUILDING_UNIT_T,
            EnumRelatableLayers.BOUNDARY: db_names.LC_BOUNDARY_T,
            EnumRelatableLayers.BOUNDARY_POINT: db_names.LC_BOUNDARY_POINT_T,
            EnumRelatableLayers.SURVEY_POINT: db_names.LC_SURVEY_POINT_T,
            EnumRelatableLayers.CONTROL_POINT: db_names.LC_CONTROL_POINT_T,
            EnumRelatableLayers.ADMINISTRATIVE_SOURCE: db_names.LC_ADMINISTRATIVE_SOURCE_T
        }

        return dict_result[self]


class EnumFeatureCreationMode(Enum):
    MANUALLY = 1,
    REFACTOR_FIELDS = 2,
    DIGITIZING_LINE = 3


class EnumFeatureSelectionType(Enum):
    SELECTION_BY_EXPRESSION = 1
    SELECTION_ON_MAP = 2
    ALL_FEATURES = 3


class EnumPlotCreationResult(Enum):
    CREATED = 1,
    NO_BOUNDARIES_SELECTED = 2,
    NO_PLOTS_CREATED = 3

