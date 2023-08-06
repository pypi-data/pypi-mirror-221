from pysidra.api.controllers.controllers import Controllers
from pysidra.api.controllers.util import get_response, get_url, get_request_params, json


class Inference:
    def __init__(self, endpoint, token):
        self._controllers = Controllers(endpoint, token)
        self.token = token
        self.endpoint = endpoint

    def sql_query(self, query, connectionString, idProvider, idDataStorageUnit, store):
        """
        Infers Entities and Attributes from a SQL query. If query is not provided, the entire DB is
         inferred.

        Parameters
        ----------
            query: string.
            connectionString: string.
            idProvider: integer.
            idDataStorageUnit: integer.
            store: boolean: Default is True.
        Returns
        -------
            JSON response.
        """
        return get_response(
            data=json.dumps(get_request_params(locals().items())),
            url=self.endpoint + get_url(),
            headers={"Content-Type": "application/json"},
            token=self.token,
            method="POST",
        ).text

    def get_datatype(self, fileUri, hasHeader=True):
        """
        Infers data types from the content of a file.

        Parameters
        ----------
            fileUri: string.
            hasHeader: boolean: Default is True.
        Returns
        -------
            JSON response.
        """
        return get_response(
            data=json.dumps(get_request_params(locals().items())),
            url=self.endpoint + get_url(),
            headers={"Content-Type": "application/json"},
            token=self.token,
            method="POST",
        ).text
