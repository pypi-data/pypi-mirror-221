import time
from typing import List, Dict
from pysidra.api.controllers.controllers import ControllerGetList, ControllerGetById
from pysidra.api.controllers.modelserving.common import KeyValueParameter, DeleteMode, ClusterJobParams, \
    ClusterJobDynamicParams, RunLifeCycleState
from pysidra.api.controllers.util import get_response, get_url, json, prepare_dict_from_obj

from pysidra.api.models.modelserving.modelversion import ModelVersion

DEFAULT_TIMEOUT = 1800

FAKE_MODELVERSION_ID = '00000000-0000-0000-0000-000000000000'


class CreateImageRequest(ClusterJobDynamicParams):
    def __init__(
            self,
            runId: str,
            idModel: str,
            imageName: str = None,
            runName: str = None,
            parameters: List[KeyValueParameter] = None,
            clusterId: str = None,
            timeOutSeconds: int = None,
    ):
        super().__init__(parameters, clusterId, timeOutSeconds)
        self.runId = runId
        self.idModel = idModel
        self.imageName = imageName
        self.runName = runName


class DeployRequest(ClusterJobDynamicParams):
    def __init__(
            self,
            runId: str = None,
            computeType: str = None,
            modelVersionId: str = None,
            parameters: List[KeyValueParameter] = None,
            clusterId: str = None,
            timeOutSeconds: int = None,
    ):
        super().__init__(parameters, clusterId, timeOutSeconds)
        self.runId = runId
        self.computeType = computeType
        self.modelVersionId = modelVersionId


class InferenceRequest(ClusterJobDynamicParams):
    def __init__(
            self,
            runId: str,
            runName: str = None,
            parameters: List[KeyValueParameter] = None,
            clusterId: str = None,
            timeOutSeconds: int = None,
    ):
        super().__init__(parameters, clusterId, timeOutSeconds)
        self.runId = runId
        self.runName = runName
        self.modelName = "model"


class ModelVersionController(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint: str, token: str):
        super().__init__(endpoint, token, instance_class=ModelVersion)

    def wait_for_job(
            self, datastorageunitId: int, jobRunId: int, timeOutSeconds: int = None
    ) -> None:
        """
        Method to wait a Cluster Job to finish.

        :param datastorageunitId: id of the DataStorageUnit
        :param jobRunId: job id
        :param timeOutSeconds: timeout
        :return:
        """
        timeout = DEFAULT_TIMEOUT if timeOutSeconds is None else timeOutSeconds
        t_init = time.time()
        status = self.job_status(datastorageunitId, jobRunId)
        while status["metadata"]["state"]["life_cycle_state"] not in [
            RunLifeCycleState.TERMINATED.value,
            RunLifeCycleState.SKIPPED.value,
            RunLifeCycleState.INTERNAL_ERROR.value,
        ]:
            print(status)
            print("Waiting for finishing job {}. {}"
                  .format(jobRunId, RunLifeCycleState(status["metadata"]["state"]["life_cycle_state"]).name))
            time.sleep(60)
            if time.time() - t_init > timeout:
                break
            status = self.job_status(datastorageunitId, jobRunId)

        # Read status again due to break statement.
        status = self.job_status(datastorageunitId, jobRunId)
        print("Finished wait for job. Status: {}".format(status))

    def create(self, modelVersion: ModelVersion) -> ModelVersion:
        """
        It creates a ModelVersions

        :type modelVersion: ModelVersion
        :param modelVersion: ModelVersion
        :return: ModelVersionResponse object.
        """
        if modelVersion is None:
            raise ValueError("modelVersion is mandatory")
        if modelVersion.idModel is None:
            raise ValueError("The Id of the model is mandatory.")
        if modelVersion.experimentId is None:
            raise ValueError("The Id of the experiment is mandatory.")
        if modelVersion.runId is None:
            raise ValueError("The Id of the run is mandatory.")

        request_body = prepare_dict_from_obj(modelVersion, exclude=["id", "model"])

        response_str = get_response(
            data=json.dumps(request_body),
            url=self._controllers.endpoint + get_url(),
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text
        result = ModelVersion(**json.loads(response_str))

        return result

    def update(self, modelVersion: ModelVersion) -> ModelVersion:
        """
        It updates a given ModelVersions

        :type modelVersion: ModelVersion
        :param modelVersion: values of ModelVersion to modify
        :return: ModelVersionResponse object.
        """
        if modelVersion.id is None:
            raise ValueError("The ModelVersion id is mandatory")

        request_url = self._controllers.endpoint + get_url().format(modelVersion.id)

        request_body = prepare_dict_from_obj(modelVersion, exclude=["id", "model"])

        response_str = get_response(
            data=json.dumps(request_body),
            url=request_url,
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="PUT",
        ).text

        result = ModelVersion(**json.loads(response_str))

        return result

    def patch(self, modelVersionId: str, dictAttributes: Dict) -> ModelVersion:
        """
        It patches a model version (partial update)
        :param modelVersionId: id of the ModelVersion to patch
        :param dictAttributes: attributes to modify
        :return: updated ModelVersion
        """
        if modelVersionId is None:
            raise ValueError("The ModelVersion id is mandatory")
        if dictAttributes is None:
            raise ValueError("dictAttributes is mandatory")

        modelVersion = self.get_by_id(modelVersionId)

        if len(dictAttributes) == 0:
            print("Nothing to patch")
        else:
            for key, value in dictAttributes.items():
                modelVersion.__setattr__(key, value)

            self.update(modelVersion)

        return modelVersion

    def delete_async(
            self,
            modelVersion: ModelVersion,
            datastorageunitId: int,
            deleteMode: int = None,
            clusterJobParams: ClusterJobParams = None,
    ) -> int:
        """
        Delete a ModelVersion with an asynchronous request

        :type modelVersion: ModelVersion
        :param modelVersion: ModelVersion to delete
        :param datastorageunitId: id of the DataStorageUnit
        :param model_version:
        :param deleteMode:
        :type clusterJobParams: ClusterJobParams
        :param clusterJobParams:

        :return: ModelVersionResponse
        """
        if modelVersion.id is None:
            raise ValueError("ModelVersion id is mandatory")
        if deleteMode is None:
            deleteMode = DeleteMode.Nothing.value

        if clusterJobParams is None:
            url_params = {}
        else:
            url_params = clusterJobParams.__dict__.copy()
        url_params["deleteMode"] = deleteMode

        response = get_response(
            url=self._controllers.endpoint + get_url().format(modelVersion.id, datastorageunitId),
            params=url_params,
            token=self._controllers.token,
            method="DELETE",
        )
        if response.ok:
            print("Model Version {} was successfully deleted".format(modelVersion.id))
        else:
            print(
                "There was an error while deleting model version {}".format(
                    modelVersion.id
                )
            )

        result = json.loads(response.text)

        return result["run_id"]

    def delete(
            self,
            modelVersion: ModelVersion,
            datastorageunitId: int,
            deleteMode: int = None,
            clusterJobParams: ClusterJobParams = None,
    ) -> None:
        """
        Delete a ModelVersion

        :type modelVersion: ModelVersion
        :param modelVersion: ModelVersion to delete
        :param datastorageunitId: id of the DataStorageUnit
        :param model_version:
        :param deleteMode:
        :type clusterJobParams: ClusterJobParams
        :param clusterJobParams:

        :return: ModelVersionResponse
        """

        time_out_seconds = None if clusterJobParams is None else clusterJobParams.timeOutSeconds

        run_job_id = self.delete_async(
            modelVersion, datastorageunitId, deleteMode, clusterJobParams
        )
        self.wait_for_job(datastorageunitId, run_job_id, timeOutSeconds=time_out_seconds)

    def create_image_async(self, datastorageunitId: int, request: CreateImageRequest) -> int:
        """
        Creates a docker image given a run id
        :param datastorageunitId: id of the DataStorageUnit
        :param request: body of create image request
        :return: run id of the Databrick's job that creates the Docker image
        """

        if datastorageunitId is None:
            raise ValueError("The datastorageunit id is mandatory")
        if request.idModel in [None, ""] or request.runId in [None, ""]:
            raise ValueError("idModel or runId is mandatory")

        response_str = get_response(
            data=json.dumps(request.__dict__.copy()),
            url=self._controllers.endpoint + get_url().format(datastorageunitId),
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text

        result = json.loads(response_str)

        return result["run_id"]

    def create_image(self, datastorageunitId: int, request: CreateImageRequest) -> ModelVersion:
        """
        Creates a docker image given a run id
        :param datastorageunitId: id of the DataStorageUnit
        :param request: body of create image request
        :return: run id of the Databrick's job that creates the Docker image
        """
        run_job_id = self.create_image_async(datastorageunitId, request)
        self.wait_for_job(datastorageunitId, run_job_id, request.timeOutSeconds)
        status = self.job_status(datastorageunitId, run_job_id)
        modelVersionId = status["metadata"]["task"]["notebook_task"]["base_parameters"]["modelVersionId"]

        return self.get_by_id(modelVersionId)

    def deploy_async(self, datastorageunitId: int, request: DeployRequest) -> int:
        """
        Deploy a docker image associated with a ModelVersion
        :param request: body of create image request
        :param datastorageunitId: id of the DataStorageUnit
        :return: run id of the Databrick's job that creates the Docker image
        """

        if request.modelVersionId in [None, ""] and request.runId in [None, ""]:
            raise ValueError("modelVersionId or runId is mandatory")
        if datastorageunitId is None:
            raise ValueError("The datastorageunit id is mandatory")

        request_url = self._controllers.endpoint + get_url().format(datastorageunitId)

        request_dict = prepare_dict_from_obj(request, excludeNone=True)

        response_str = get_response(
            data=json.dumps(request_dict),
            url=request_url,
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text

        result = json.loads(response_str)

        return int(result["run_id"])

    def deploy(self, datastorageunitId: int, request: DeployRequest) -> ModelVersion:
        """
        Deploy a docker image associated with a ModelVersion
        :param request: body of create image request
        :param datastorageunitId: id of the DataStorageUnit
        :return: run id of the Databrick's job that creates the Docker image
        """
        run_job_id = self.deploy_async(datastorageunitId, request)
        self.wait_for_job(datastorageunitId, run_job_id, request.timeOutSeconds)
        status = self.job_status(datastorageunitId, run_job_id)
        modelVersionId = status["metadata"]["task"]["notebook_task"]["base_parameters"]["modelVersionId"]

        return self.get_by_id(modelVersionId)

    def undeploy_async(
            self,
            modelVersion: ModelVersion,
            datastorageunitId: int,
            request: ClusterJobParams = type("", (), {})(),
    ) -> int:
        """
        It undeploys a webservice associated with a ModelVersion
        :param modelVersion: ModelVersion to undeploy
        :param datastorageunitId: id of the DataStorageUnit
        :param request: cluster params
        :return: run id of the Databrick's job that creates the Docker image
        """

        if modelVersion.id in [None, ""]:
            raise ValueError("A ModelVersion is mandatory")
        if datastorageunitId is None:
            raise ValueError("The datastorageunit id is mandatory")

        request_url = self._controllers.endpoint + get_url().format(modelVersion.id, datastorageunitId)

        response_str = get_response(
            data=json.dumps(request.__dict__.copy()),
            url=request_url,
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text

        result = json.loads(response_str)

        return int(result["run_id"])

    def undeploy(
            self,
            modelVersion: ModelVersion,
            datastorageunitId: int,
            request: ClusterJobParams = type("", (), {})(),
    ) -> None:
        """
        It undeploys a webservice associated with a ModelVersion
        :param modelVersion: ModelVersion to undeploy
        :param datastorageunitId: id of the DataStorageUnit
        :param request: cluster params
        :return: run id of the Databrick's job that creates the Docker image
        """
        run_job_id = self.undeploy_async(modelVersion, datastorageunitId, request)
        if 'timeOutSeconds' in request.__dict__:
            self.wait_for_job(datastorageunitId, run_job_id, request.timeOutSeconds)
        else:
            self.wait_for_job(datastorageunitId, run_job_id)

    def inference_async(self, modelVersionId: str, datastorageunitId: int, request: InferenceRequest, ) -> int:
        """
        It executes a model
        :param modelVersionId: id of the ModelVersion
        :param datastorageunitId: id of the DataStorageUnit
        :param request: body to execute the inference
        :return: run id of the Databrick's job that execute the inference
        """

        if datastorageunitId is None:
            raise ValueError("The datastorageunit id is mandatory")

        if request is None:
            raise ValueError("request is mandatory")

        request_url = self._controllers.endpoint + get_url().format(modelVersionId, datastorageunitId)

        request_dict = prepare_dict_from_obj(request, excludeNone=True)

        response_str = get_response(
            url=request_url,
            data=json.dumps(request_dict),
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text

        result = json.loads(response_str)

        return int(result["run_id"])

    def inference(self, modelVersionId: str, datastorageunitId: int, request: InferenceRequest, ) -> None:
        """
        It executes a model
        :param modelVersionId: id of the ModelVersion
        :param datastorageunitId: id of the DataStorageUnit
        :param request: body to execute the inference
        :return: run id of the Databrick's job that execute the inference
        """
        run_job_id = self.inference_async(modelVersionId, datastorageunitId, request)
        self.wait_for_job(datastorageunitId, run_job_id, request.timeOutSeconds)

    def job_status(self, datastorageunitId: int, jobRunId: int) -> Dict:
        """
        It executes a model
        :param datastorageunitId: id of the DataStorageUnit
        :param jobRunId: body to execute the inference
        :return: run id of the Databrick's job that execute the inference
        """

        if datastorageunitId is None:
            raise ValueError("DataStorageUnit id is mandatory")
        if jobRunId is None:
            raise ValueError("jobRunId is mandatory")

        request_url = self._controllers.endpoint + get_url().format(FAKE_MODELVERSION_ID, datastorageunitId, jobRunId)

        response_str = get_response(
            url=request_url,
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="GET",
        ).text

        response_dict = json.loads(response_str)

        return response_dict
