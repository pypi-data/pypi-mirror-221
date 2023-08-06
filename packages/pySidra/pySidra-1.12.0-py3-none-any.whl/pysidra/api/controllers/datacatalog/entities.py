import json
from typing import List

from pysidra.api.controllers.controllers import ControllerGetList, ControllerGetById
from pysidra.api.controllers.util import get_response, get_url


class Entities(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)

    def get_with_attributes(self, ids):
        """
        Gets a list of Entities filtered by their Ids, with their attributes.

        Parameters
        ----------
            ids: list: Ids of Entities to find. This parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        # Check input arguments.
        if ids is None:
            raise ValueError("ids is required")

        return get_response(
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
            headers={"Content-Type": "application/json"},
            data=json.dumps(ids),
            method="GET",
        ).text

    def update_deployment_date(self, ids):
        """
        Update the specified entities' deployment date to today's date.

        Parameters
        ----------
            ids: list: Ids of Entities to find. This parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        # Check input arguments.
        if ids is None:
            raise ValueError("ids is required")

        return get_response(
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
            headers={"Content-Type": "application/json"},
            data=json.dumps(ids),
            method="PUT",
        ).text

    def update_recreate_table(self, ids, recreateTable):
        """
        Update the specified entities' table recreation for the next deployment. 

        Parameters
        ----------
            Request that contain the id of the entities to update and the new value for the recreate table flag.
            It looks like:
            {
                "idEntities": [ID1, ID2, ...],
                "recreateTable": true
            }
        Returns
        -------
            JSON response.
        """
        # Check input arguments.
        if ids is None:
            raise ValueError("ids is required")

        request_body = {"recreateTable": recreateTable, "idEntities": ids}
        return get_response(
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
            headers={"Content-Type": "application/json"},
            data=json.dumps(request_body),
            method="PUT",
        ).text



    def get_pipelines(self, idEntity: int) -> List:
        """
        Get all pipelines associated with the specific Entity.

        :param idEntity: Id of Entity to get the pipelines. This parameter is mandatory.
        :return: list of pipelines
        """
        return self._controllers.get_asociated_list(idEntity)

    def get_tags(self, idEntity: int) -> List:
        """
        Get all tags associated with the specific Entity.

        :param idEntity: Id of Entity to get the tags. This parameter is mandatory.
        :return: list of tags
        """
        return self._controllers.get_asociated_list(idEntity)

    def get_attributes(self, idEntity: int) -> List:
        """
        Get all attributes associated with the specific Entity.

        :param idEntity: Id of Entity to get the attributes. This parameter is mandatory.
        :return: list of attributes
        """
        return self._controllers.get_asociated_list(idEntity)

    def set_attributes(self, idEntity, attributes):
        """
        Sets all the attributes associated with the Entiy.

        Parameters
        ----------
            idEntity: integer: Id of Entity to get the tags. This parameter is mandatory.
            attributes: Attributes array.
        Returns
        -------
            JSON response
        """
        if idEntity is None:
            raise ValueError("idEntity is required")

        for attribute in attributes:
            attribute["idEntity"] = idEntity

        return get_response(
            url=self._controllers.endpoint + get_url().format(idEntity),
            token=self._controllers.token,
            headers={"Content-Type": "application/json"},
            data=json.dumps(attributes),
            method="PUT",
        ).text
