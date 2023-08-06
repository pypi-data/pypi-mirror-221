from pysidra.api.controllers import Constants
from pysidra.api.controllers.controllers import ControllerBase
from pysidra.api.controllers.util import get_response, get_url, get_request_params


class Service(ControllerBase):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token)

    def get_clusters(self):
        """
        Get a list of all Clusters.

        Returns
        -------
            JSON response.
        """
        return self._controllers.get_status_list()

    def get_services(self):
        """
        Get a list of all services.

        Returns
        -------
            JSON response.
        """
        return self._controllers.get_status_list()

    def get_datastorageunits(self):
        """
        Get a list of all Data Storage Units.

        Returns
        -------
            JSON response.
        """
        return self._controllers.get_status_list()

    def get_count_errors(self, offsetId):
        """
        Get a count of the errors from log.

        Parameters
        ----------
            offsetId: integer: Only entries with Id greater than offsetId will be used. This
                      parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        return self._controllers.get_asociated_list(offsetId)

    def get_count_warnings(self, offsetId):
        """
        Get a count of the warnings from log.

        Parameters
        ----------
            offsetId: integer: Only entries with Id greater than offsetId will be used. This
                      parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        return self._controllers.get_asociated_list(offsetId)

    def get_last_warnings(self, numberOfItems=3):
        """
        Get last warnings.

        Parameters
        ----------
            numberOfItems: integer: number of warnings to retrieve. Default value: 3.
        Returns
        -------
            JSON response.
        """
        return self._controllers.get_number_items(numberOfItems)

    def get_last_errors(self, numberOfItems=3):
        """
        Get last errors.

        Parameters
        ----------
            numberOfItems: integer: number of warnings to retrieve. Default value: 3.
        Returns
        -------
            JSON response.
        """
        return self._controllers.get_number_items(numberOfItems)

    def get_count_log(self, offsetId=None, severities=None):
        """
        Get a count of the entries from log, grouped by severity and, optionally filtered by
        severity. The result is a dictionary severity-count.

        Parameters
        ----------
            offsetId: integer: Only entries with Id greater than offsetId will be used. This
                      parameter is mandatory.
            severities: array[string]: Severities expected on the log entries, if not specified,
                        all of them are recovered. This parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        # Check input arguments
        if offsetId is None:
            raise ValueError("offsetid is mandatory")

        return get_response(
            params=get_request_params(locals().items()),
            url=self._controllers.endpoint + get_url().format(offsetId),
            token=self._controllers.token,
        ).text

    def get_measure(self, measure="totalApps"):
        """
        Get measure from available list.

        Parameters
        ----------
            measure: array[string]: Available values : totalApps, storageVolume, lastDayVolume,
                     totalEntities, totalRows, totalStreamingSources, totalAssets,
                     totalDataStorageUnitRegions, totalProviders.This parameter is mandatory.
        Returns
        -------
            JSON response.
        """
        # Check input arguments
        if measure not in Constants.MEASURES_LIST:
            raise ValueError(
                "'measure' have to be one of these: {}".format(Constants.MEASURES_LIST)
            )

        return get_response(
            params=get_request_params(locals().items()),
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
        ).text

    def get_daily_measures(self, measure=None, startDate=None, endDate=None):
        """
        Return a list of dated measure values between two dates.

        Parameters
        ----------
            measure: array[string]: names of the measures to retrieve. Available values:
                     validationErrors, loadVolume. This parameter is mandatory.
            startDate: string(date-time): first date to retrieve in measures list. In
                       {YYYY-MM-dd HH:mm:ss} format.
            endDate: string(date-time): last date to retrieve in measures list. In
                     {YYYY-MM-dd HH:mm:ss} format.
        Returns
        -------
            JSON response
        """
        # Check input arguments
        if startDate is not None:
            startDate = startDate.replace(" ", "%20").replace(":", "%3A")
        if endDate is not None:
            endDate = endDate.replace(" ", "%20").replace(":", "%3A")
        if measure not in Constants.DAILY_MEASURES_LIST:
            raise ValueError(
                "'measure' have to be one of these: {}".format(
                    Constants.DAILY_MEASURES_LIST
                )
            )

        return get_response(
            params=get_request_params(locals().items()),
            url=self._controllers.endpoint + get_url(),
            token=self._controllers.token,
        ).text
