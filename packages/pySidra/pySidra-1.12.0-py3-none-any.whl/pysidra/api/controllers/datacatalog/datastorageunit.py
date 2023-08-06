from pysidra.api.controllers.controllers import ControllerGetById, ControllerGetList


class DataStorageUnit(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)
