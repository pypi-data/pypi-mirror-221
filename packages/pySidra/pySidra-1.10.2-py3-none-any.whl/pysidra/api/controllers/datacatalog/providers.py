from typing import List

from pysidra.api.controllers.controllers import ControllerGetList, ControllerGetById


class Providers(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)

    def get_tags(self, providersId: int) -> List:
        """
        Gets tag of a provider.

        :param providersIds:
        :return: list of tags
        """
        return self._controllers.get_asociated_list(providersId)
