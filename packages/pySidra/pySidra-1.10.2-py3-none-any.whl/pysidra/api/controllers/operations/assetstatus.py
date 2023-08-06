from pysidra.api.controllers import Controllers


class AssetStatus:
    def __init__(self, endpoint, token):
        self._controllers = Controllers(endpoint, token)

    def get_status_list(self):
        """
        Get the list of status that an asset can have.

        Returns
        -------
            JSON response.
        """
        return self._controllers.get_status_list()
