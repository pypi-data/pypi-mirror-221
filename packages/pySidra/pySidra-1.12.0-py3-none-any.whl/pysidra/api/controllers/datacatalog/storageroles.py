from pysidra.api.controllers.controllers import ControllerGetList, ControllerGetById


class StorageRoles(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)