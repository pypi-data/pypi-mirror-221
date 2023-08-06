import os
import urllib
import zipfile

import pandas as pd

from pysidra.api.controllers import Controllers
from pysidra.api.controllers.datacatalog import Entities
from pysidra.api.controllers.util import *


class Query:
    """
    WARNING: Methods of this class are deprecated.
    """
    def __init__(self, endpoint, token):
        self._controllers = Controllers(endpoint, token)
        self.Entities = Entities(endpoint, token)
        self.token = token
        self.endpoint = endpoint

    def get_stream(self, pollingToken):
        """
        Gets the information of the execution status of a query and the System.IO.Stream to
         access to the results in case it has finished.

        Parameters
        ----------
            pollingToken: string: The polling token that contains the information about the
                          query execution to check. This parameter is mandatory.
            expirationInHours: integer: Expiration of the token provided. By default is None.
        Returns
        -------
            System.IO.Stream.
        """
        return self._controllers.check_pollintoken(pollingToken)

    def get_status(self, pollingToken, expirationInHours=1):
        """
        Gets the information of the execution status of a query and the SAS tokens to access
         to the results in case it has finished.

        Parameters
        ----------
            pollingToken: string: The polling token that contains the information about the
                          query execution to check. This parameter is mandatory.
            expirationInHours: integer: Expiration of the token provided. By default is 1 hour.
        Returns
        -------
            sasToken as JSON response.
        """
        return self._controllers.check_pollintoken(pollingToken, expirationInHours)

    def get_prefilter(
        self,
        idEntity=None,
        commaSeparatedColumns=None,
        filterExpression=None,
        distributedBy=None,
        queryOutputFormat="text",
        outputColumnSplitter="\\u0002",
        idSourceItems=None,
        lastExportedAssetIds=None,
        commaSeparatedFilterColumns=None,
        addRowsWithSame=None,
    ):
        """
        Compose a query based on the parameters provided and execute it.

        Parameters
        ----------
            idEntity: integer: The Id of the Entity from which get the information to create the
                      query. This parameter is mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is mandatory.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
            lastExportedAssetIds: array[integer]: Array of ids of SourceItems of the latest exported
                                  assets. This parameter is mandatory.
            addRowsWithSame: string: Indicates the column names that define if a register is equal
                             to another.
        Returns
        -------
            pollingToken as JSON response.
        """
        # Check input arguments.
        if idEntity is None:
            raise ValueError("idEntity is required and have to be an integer")
        if commaSeparatedColumns is None:
            raise ValueError("commaSeparatedColumns is mandatory")
        if lastExportedAssetIds is None:
            raise ValueError("lastExportedAssetIds is required")
        if not isinstance(lastExportedAssetIds, list):
            raise ValueError("lastExportedAssetIds is an integer array")
        if commaSeparatedFilterColumns is None:
            raise ValueError("commaSeparatedFilterColumns is required")
        if queryOutputFormat not in ("text", "parquet"):
            raise ValueError("queryOutputFormat is either 'text' or 'parquet'")
        if idSourceItems is not None:
            if not isinstance(idSourceItems, list):
                raise ValueError("idSourceItems is an integer array")

        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url().format(idEntity),
            token=self.token,
        ).text

    def get_execute(
        self,
        databaseName=None,
        tableName=None,
        commaSeparatedColumns=None,
        filterExpression=None,
        distributedBy=None,
        queryOutputFormat="text",
        outputColumnSplitter="\\u0002",
        idSourceItems=None,
    ):
        """
        Compose a query based on the parameters provided and execute it.

        Parameters
        ----------
            tableName: string: The name of the table to which query. This parameter is mandatory.
            databaseName: string: The name of the database to which query. This parameter is
                          mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is mandatory.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
        Returns
        -------
            pollingToken as JSON response.
        """
        # Check input arguments.
        if databaseName is None:
            raise ValueError("databaseName is required")
        if tableName is None:
            raise ValueError("tableName is required")
        if commaSeparatedColumns is None:
            raise ValueError("commaSeparatedColumns is mandatory")
        if queryOutputFormat not in ("text", "parquet"):
            raise ValueError(
                "queryOutputFormat is mandatory and is either 'text' or 'parquet'"
            )
        if idSourceItems is not None:
            if not isinstance(idSourceItems, list):
                raise ValueError("idSourceItems is an integer array")

        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url(),
            token=self.token,
        ).text

    def get_id_filter(
        self,
        idEntity=None,
        commaSeparatedColumns=None,
        filterExpression=None,
        distributedBy=None,
        queryOutputFormat="text",
        outputColumnSplitter="\\u0002",
        idSourceItems=None,
    ):
        """
        Compose a query based on the parameters provided and execute it.

        Parameters
        ----------
            idEntity: integer: The Id of the Entity from which get the information to create the
                      query. This parameter is mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is mandatory.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
        Returns
        -------
            pollingToken as JSON response.
        """
        # Check input arguments.
        if idEntity is None:
            raise ValueError("idEntity is mandatory")
        if commaSeparatedColumns is None:
            raise ValueError("commaSeparatedColumns is mandatory")
        if idSourceItems is not None:
            if not isinstance(idSourceItems, list):
                raise ValueError("idSourceItems is an integer array")
        if queryOutputFormat not in ("text", "parquet"):
            raise ValueError(
                "queryOutputFormat is mandatory and is either 'text' or 'parquet'"
            )

        return get_response(
            params=get_request_params(locals().items()),
            url=self.endpoint + get_url().format(idEntity),
            token=self.token,
        ).text

    def _get_file(self, waitTime=3600, **kwarg):
        """
        Get sasToken of an entity based on a query according with the parameters provided.

        Parameters
        ----------
            idEntity: integer: The Id of the Entity from which get the information to create the
                      query. This parameter is mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is optional.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
            waitTime: integer: Maximum time to wait for succesfull response. Default is 3600
                      seconds. This parameter is optional.
        Returns
        -------
        List with link to download files and list with columns names.
        """
        # Check input arguments.
        if "idEntity" not in kwarg.keys():
            raise ValueError("idEntity is mandatory")

        # Get commaSeparatedColumns parameter if it is not provided then request pollingtoken and
        # decode it
        if "commaSeparatedColumns" in kwarg.keys():
            column_list = kwarg["commaSeparatedColumns"]
            polling_token = json.loads(
                self.get_id_filter(
                    idEntity=kwarg["idEntity"],
                    commaSeparatedColumns=kwarg["commaSeparatedColumns"],
                )
            )
        else:
            column_list = make_columns_list(
                json.loads(self.Entities.get_attributes(idEntity=kwarg["idEntity"]))
            )
            polling_token = json.loads(
                self.get_id_filter(
                    idEntity=kwarg["idEntity"], commaSeparatedColumns=column_list
                )
            )
        polling_token = urllib.parse.unquote_plus(
            polling_token["pollingToken"], encoding="utf-8", errors="replace"
        )

        # Request sasToken every 15 seconds during waitTime seconds while the response status is not
        #  TERMINATED
        start_time = time.time()
        wait_time = start_time + waitTime
        resp = self.get_status(pollingToken=polling_token)
        result_text, result_status = check_file(response=resp)

        while result_status != "TERMINATED":

            if time_format(time.time()) == time_format(wait_time):
                raise TimeoutError("The time exceed max time")

            print("waiting for file")
            time.sleep(15)
            resp = self.get_status(pollingToken=polling_token)
            result_text, result_status = check_file(response=resp)

        if json.loads(result_text)["sasToken"] == []:
            raise InterruptedError(
                'While generating file "sasToken" was not found:\n{}, {}'.format(
                    result_status, result_text
                )
            )

        # Extract the sasToken from the json reponse and return it along with the columns names as
        #  lists
        link = json.loads(result_text)["sasToken"]
        return link, column_list

    def load_file(
        self, idEntity=None, links=None, sep="\x02", encoding="utf-8", **kwarg
    ):
        """
        Load a pandas dataframe of an Entity based on a query according with the parameters provided.

        Parameters
        ----------
            idEntity: integer: The Id of the Entity from which get the information to create the
                      query. This parameter is mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is optional.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
            links: array[string]: Array of url where download the files. This parameter is
                   optional.
            sep: string: columns separator character in file. Default is '\x02'. This parameter is
                 optional.
            encoding: string: encoding of file. Default is utf-8. This parameter is optional.
            waitTime: integer: Maximum time to wait for succesfull response. Default is 3600
                      seconds. This parameter is optional.
        Returns
        -------
            Pandas dataframe.
        """
        # Check input arguments.
        if idEntity is None:
            raise ValueError("idEntity is mandatory")

        # Get links and commaSeparatedColumns parameters if they are not provided
        if links is None:
            links, column_list = self._get_file(idEntity=idEntity)
        if links is not None and "commaSeparatedColumns" not in kwarg.keys():
            column_list = make_columns_list(
                json.loads(self.Entities.get_attributes(idEntity=idEntity))
            )
        elif links is not None and "commaSeparatedColumns" in kwarg.keys():
            column_list = kwarg["commaSeparatedColumns"]

        # Load the file links in a pandas dataframe if exceptions happend the links are printed
        df_array = []
        try:
            for url in links:
                df = pd.read_csv(
                    url,
                    sep=sep,
                    names=column_list.split(","),
                    header=None,
                    encoding=encoding,
                )
                df_array.append(df)
            return pd.concat(df_array)
        except:
            raise print(
                "Error while processing pandas dataframe,\n\
                    the file has been generated and stored in:\n{}".format(
                    links
                )
            )

    def download_file(self, filePath=None, fileName=None, waitTime=3600, **kwarg):
        """
        Download a zip file of an entity based on a query according with the parameters provided.

        Parameters
        ----------
            filename: string: Name of file to save (without extension). This parameter is mandatory.
            filepath: string: Directory to save the file, if None will be saved in current
                      directory. This parameter is optional.
            idEntity: integer: The Id of the Entity from which get the information to create the
                      query. This parameter is mandatory.
            commaSeparatedColumns: string: comma separated columns names, if None all columns will
                                   be loaded. This parameter is optional.
            filterExpression: string: Condition included in the where clause to filter the
                              selection. This parameter is optional.
            distributedBy: string: Column names used by Hive to distribute the rows among reducers.
                           All rows with the same Distribute By columns will go to the same reducer.
                            This parameter is optional.
            outputColumnSplitter: string: columns separator character in file. Default is '\\u0002'.
                                  This parameter is optional.
            queryOutputFormat: string: Indicates the output format of the extracted data. Options
                               are 'Text' or 'Parquet'. Default is 'text. This parameter is
                               optional.
            idSourceItems: array[integer]: Array of ids of SourceItems that will be used to filter
                           the selection in the where clause. This parameter is optional.
            waitTime: integer: Maximum time to wait for succesfull response. Default is 3600
                      seconds. This parameter is optional.
        Returns
        -------
            Zip file.
        """
        # Check input arguments.
        if "idEntity" not in kwarg.keys():
            raise ValueError("idEntity is mandatory")
        if fileName is None:
            raise ValueError("fileName is mandatory")

        # Build filepath either its relative or complete
        if filePath is None:
            filePath = os.getcwd()
            os.makedirs(filePath, exist_ok=True)
            directory = filePath + os.sep + fileName + ".zip"
        else:
            if os.path.isabs(filePath):
                os.makedirs(filePath, exist_ok=True)
                directory = filePath + os.sep + fileName + ".zip"
            else:
                file_path = os.getcwd() + os.sep + filePath
                os.makedirs(filePath, exist_ok=True)
                directory = file_path + os.sep + fileName + ".zip"

        # Get columns names if they are not provided
        if "commaSeparatedColumns" in kwarg.keys():
            column_list = kwarg["commaSeparatedColumns"]
        else:
            column_list = make_columns_list(
                json.loads(self.Entities.get_attributes(idEntity=kwarg["idEntity"]))
            )

        # Request pollintoken and decode it
        polling_token = json.loads(
            self.get_id_filter(
                idEntity=kwarg["idEntity"], commaSeparatedColumns=column_list
            )
        )
        polling_token = urllib.parse.unquote_plus(
            polling_token["pollingToken"], encoding="utf-8", errors="replace"
        )

        # Request bytes stream every 10 seconds during waitTime seconds and save the bytes stream as
        # zip file. Then append a new text file with columns names.
        start_time = time.time()
        wait_time = start_time + waitTime
        resp = self.get_stream(pollingToken=polling_token)

        while resp.status_code == 204 or resp.status_code == 200:
            if resp.status_code == 200:
                with open(directory, "wb") as out_file:
                    out_file.write(resp.content)
                zip_file = zipfile.ZipFile(directory, "a")
                new_file_name = "header"
                new_file_content = column_list
                zip_file.writestr(new_file_name, new_file_content, zipfile.ZIP_DEFLATED)
                zip_file.close()
                return print("File has been downloaded in: \n {}".format(directory))

            if time_format(time.time()) == time_format(wait_time):
                raise TimeoutError("The time exceed max time")

            print("waiting for file")
            time.sleep(10)
            resp = self.get_stream(pollingToken=polling_token)
