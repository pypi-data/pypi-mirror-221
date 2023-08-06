import enum


class Constants:
    API_VERSION = "1.0"
    DEBUG_REQUEST_RESPONSE = False
    MEASURES_LIST = [
        "totalApps",
        "storageVolume",
        "lastDayVolume",
        "totalEntities",
        "totalRows",
        "totalStreamingSources",
        "totalAssets",
        "totalDataStorageUnitRegions",
        "totalProviders",
    ]
    DAILY_MEASURES_LIST = ["validationErrors", "loadVolume"]
    ATTRIBUTES_TO_AVOID_IN_PARAMS = ["id", "self", "offsetId", "idEntity"]
    URL_ATTRIBUTES_GET_LIST = "/api/metadata/attributes"
    URL_ATTRIBUTES_GET_BY_ID = "/api/metadata/attributes/{}"
    URL_DATASTORAGEUNIT_GET_LIST = "/api/datastorageunit/DataStorageUnits"
    URL_DATASTORAGEUNIT_GET_BY_ID = "/api/datastorageunit/DataStorageUnits/{}"
    URL_ENTITIES_GET_LIST = "/api/metadata/Entities"
    URL_ENTITIES_GET_BY_ID = "/api/metadata/Entities/{}"
    URL_ENTITIES_GET_WITH_ATTRIBUTES = "/api/metadata/Entities/withattributes"
    URL_ENTITIES_UPDATE_RECREATE_TABLE = "/api/metadata/Entities/updaterecreatetable"
    URL_ENTITIES_UPDATE_DEPLOYMENT_DATE = "/api/metadata/Entities/updatedeploymentdate"
    URL_ENTITIES_GET_PIPELINES = "/api/metadata/Entities/{}/pipelines"
    URL_ENTITIES_GET_TAGS = "/api/metadata/Entities/{}/tags"
    URL_ENTITIES_GET_ATTRIBUTES = "/api/metadata/Entities/{}/attributes"
    URL_ENTITIES_SET_ATTRIBUTES = "/api/metadata/Entities/{}/attributes"
    URL_PROVIDERS_GET_LIST = "/api/metadata/Providers"
    URL_PROVIDERS_GET_BY_ID = "/api/metadata/Providers/{}"
    URL_PROVIDERS_GET_TAGS = "/api/metadata/Providers/{}/tags"
    URL_TAGS_GET_LIST = "/api/metadata/Tags"
    URL_QUERY_GET_ID_FILTER = "/api/Query/entity/{}"
    URL_QUERY_GET_PREFILTER = "/api/Query/entity/{}/prefiltered"
    URL_QUERY_GET_EXECUTE = "/api/Query/execute"
    URL_QUERY_GET_STATUS = "/api/Query/result/sas"
    URL_QUERY_GET_STREAM = "/api/Query/result/stream"
    URL_INFERENCE_SQL_QUERY = "/api/Inference/sqlinference"
    URL_INFERENCE_GET_DATATYPE = "/api/Inference/datatype"
    URL_ASSETS_GET_LIST = "/api/metadata/Assets"
    URL_ASSETS_GET_BY_ID = "/api/metadata/Assets/{}"
    URL_ASSETSTATUS_GET_STATUS_LIST = "/api/metadata/AssetStatus"
    URL_SERVICE_GET_CLUSTERS = "/api/Service/clusters"
    URL_SERVICE_GET_SERVICES = "/api/Service/services"
    URL_SERVICE_GET_DATASTORAGEUNITS = "/api/Service/datastorageunits"
    URL_SERVICE_GET_LAST_ERRORS = "/api/Service/lasterrors"
    URL_SERVICE_GET_LAST_WARNINGS = "/api/Service/lastwarnings"
    URL_SERVICE_GET_COUNT_ERRORS = "/api/Service/errorscount/{}"
    URL_SERVICE_GET_COUNT_WARNINGS = "/api/Service/warningscount/{}"
    URL_SERVICE_GET_COUNT_LOG = """/api/Service/logcount/{}/{{severities}}"""
    URL_SERVICE_GET_MEASURE = "/api/Service/measures/{{measures}}"
    URL_SERVICE_GET_DAILY_MEASURES = "/api/Service/dailymeasures/{{measures}}"
    URL_MODELCONTROLLER_GET_LIST = "/api/ModelServing/Model"
    URL_MODELCONTROLLER_GET_BY_ID = "/api/ModelServing/Model/{}"
    URL_MODELCONTROLLER_CREATE = "/api/ModelServing/Model"
    URL_MODELCONTROLLER_UPDATE = "/api/ModelServing/Model/{}"
    URL_MODELCONTROLLER_DELETE_ASYNC = "/api/ModelServing/Model/{}/datastorageunit/{}"
    URL_MODELVERSIONCONTROLLER_GET_LIST = "/api/ModelServing/ModelVersion"
    URL_MODELVERSIONCONTROLLER_GET_BY_ID = "/api/ModelServing/ModelVersion/{}"
    URL_MODELVERSIONCONTROLLER_CREATE = "/api/ModelServing/ModelVersion"
    URL_MODELVERSIONCONTROLLER_UPDATE = "/api/ModelServing/ModelVersion/{}"
    URL_MODELVERSIONCONTROLLER_DELETE_ASYNC = "/api/ModelServing/ModelVersion/{}/datastorageunit/{}"
    URL_MODELVERSIONCONTROLLER_CREATE_IMAGE_ASYNC = "/api/ModelServing/ModelVersion/datastorageunit/{}/image"
    URL_MODELVERSIONCONTROLLER_DEPLOY_ASYNC = "/api/ModelServing/ModelVersion/datastorageunit/{}/deploy"
    URL_MODELVERSIONCONTROLLER_UNDEPLOY_ASYNC = "/api/ModelServing/ModelVersion/{}/datastorageunit/{}/undeploy"
    URL_MODELVERSIONCONTROLLER_INFERENCE_ASYNC = "/api/ModelServing/ModelVersion/{}/datastorageunit/{}/inference"
    URL_MODELVERSIONCONTROLLER_JOB_STATUS = "/api/ModelServing/ModelVersion/{}/datastorageunit/{}/job/{}/status"
    URL_STORAGES_GET_LIST = "/api/datastorageunit/Storages"
    URL_STORAGES_GET_BY_ID = "/api/datastorageunit/Storages/{}"
    URL_STORAGEROLES_GET_LIST = "/api/datastorageunit/StorageRoles"
    URL_STORAGEROLES_GET_BY_ID = "/api/datastorageunit/StorageRoles/{}"


class EntityType(enum.Enum):
    Other = 0
    Table = 1
    View = 2
