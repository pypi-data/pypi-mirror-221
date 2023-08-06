from pysidra.api.controllers.controllers import ControllerGetList


class Tags(ControllerGetList):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)
