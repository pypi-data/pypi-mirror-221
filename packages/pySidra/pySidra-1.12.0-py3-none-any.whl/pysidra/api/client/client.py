from pysidra.api.controllers import datacatalog
from pysidra.api.controllers import integration
from pysidra.api.controllers import operations
from pysidra.api.controllers import modelserving


class Datacatalog(object):
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.Attributes = datacatalog.Attributes(endpoint, token)
        self.DataStorageUnit = datacatalog.DataStorageUnit(endpoint, token)
        self.Entities = datacatalog.Entities(endpoint, token)
        self.Providers = datacatalog.Providers(endpoint, token)
        self.Tags = datacatalog.Tags(endpoint, token)
        self.Storages = datacatalog.Storages(endpoint, token)
        self.StorageRoles = datacatalog.StorageRoles(endpoint, token)


class Integration(object):
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.Query = integration.Query(endpoint, token)
        self.Inference = integration.Inference(endpoint, token)


class ModelServing(object):
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.Model = modelserving.ModelController(endpoint, token)
        self.ModelVersion = modelserving.ModelVersionController(endpoint, token)


class Operations(object):
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.AssetStatus = operations.AssetStatus(endpoint, token)
        self.Assets = operations.Assets(endpoint, token)
        self.Service = operations.Service(endpoint, token)


class Client(object):
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.Operations = Operations(endpoint, token)
        self.Integration = Integration(endpoint, token)
        self.Datacatalog = Datacatalog(endpoint, token)
        self.ModelServing = ModelServing(endpoint, token)
