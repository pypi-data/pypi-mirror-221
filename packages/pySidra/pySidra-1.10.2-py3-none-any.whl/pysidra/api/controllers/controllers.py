import json
from typing import List, Generic, TypeVar

from pysidra.api.controllers.util import get_response, get_url, get_request_params, prepare_dict_from_obj
from pysidra.api.models.common.pagination import FiltersPaginationRequest, FiltersPaginationResponse

T = TypeVar('T')


class ControllerBase(Generic[T]):
    def __init__(self, endpoint: str, token: str, instance_class: T = None):
        self._controllers = Controllers(endpoint, token)
        self._instance_class = instance_class


class ControllerGetList(ControllerBase):
    def __init__(self, endpoint, token, instance_class: T = None):
        super().__init__(endpoint, token, instance_class)

    def get_list(self, request: FiltersPaginationRequest = None) -> FiltersPaginationResponse:

        response_str = get_response(
            params=prepare_dict_from_obj(request, excludeNone=True),
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
        ).text

        response = FiltersPaginationResponse(**json.loads(response_str))
        if self._instance_class is not None:
            result = []
            for item_dict in response.items:
                item_instance = self._instance_class(**item_dict)
                result.append(item_instance)
            response.items = result

        return response


class ControllerGetById(ControllerBase):
    def __init__(self, endpoint, token, instance_class: T = None):
        super().__init__(endpoint, token, instance_class)

    def get_by_id(self, identifier: str) -> T:
        # Check input arguments.
        if identifier is None:
            raise ValueError("id is required")

        result = get_response(
            url=self._controllers.endpoint + get_url().format(identifier),
            token=self._controllers.token,
        ).text

        if self._instance_class is not None:
            response = json.loads(result)
            result = self._instance_class(**response)

        return result


class Controllers:
    def __init__(self, endpoint, token):
        self.token = token
        self.endpoint = endpoint

    def get_asociated_list(self, identifier: int) -> List:
        """
        Get all pipelines associated with the specific Entity.

        :param idEntity: Id of Entity to get the pipelines. This parameter is mandatory.
        :return: list of pipelines
        """
        if identifier is None:
            raise ValueError("identifier is mandatory")

        return get_response(
            url=self.endpoint + get_url().format(identifier),
            token=self.token,
        ).text

    def get_status_list(self):
        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url(),
            token=self.token,
        ).text

    def get_number_items(self, numberOfItems):
        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url(),
            token=self.token,
        ).text

    def check_pollintoken(self, pollingToken, expirationInHours=None):
        # Check input arguments
        if pollingToken is None:
            raise ValueError("pollingToken is mandatory")

        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url(),
            token=self.token,
        )
