from typing import List, Dict

from pysidra.api.controllers.controllers import ControllerGetById, ControllerGetList
from .modelversion import ModelVersionController
from pysidra.api.controllers.modelserving.common import ClusterJobParams, DeleteMode
from pysidra.api.controllers.util import get_response, get_url, get_request_params, json, prepare_dict_from_obj
from pysidra.api.models.modelserving.model import Model


class ModelController(ControllerGetList, ControllerGetById):
    def __init__(self, endpoint, token):
        super().__init__(endpoint, token, instance_class=Model)
        self.modelversioncontroller = ModelVersionController(endpoint, token)

    def create(self, model: Model) -> Model:
        """
        It creates a new model

        :type model: Model
        :param model: Model
        :return: the created Model
        """
        if model is None:
            raise ValueError("model is mandatory")
        if model.name is None:
            raise ValueError("Model name is required.")

        request_body = prepare_dict_from_obj(model, exclude=["id", "versions"])

        response = get_response(
            data=json.dumps(request_body),
            url=self._controllers.endpoint + get_url(),
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="POST",
        ).text
        response_str = json.loads(response)
        result = Model(**response_str)

        return result

    def update(self, model: Model) -> Model:
        """
        It updates a new model

        :param model: Model
        :return: the created Model
        """
        if model.id is None:
            raise ValueError("The model id is required")

        request_url = self._controllers.endpoint + get_url().format(model.id)

        request_body = prepare_dict_from_obj(model, exclude=["id", "versions"])

        response_str = get_response(
            data=json.dumps(request_body),
            url=request_url,
            headers={"Content-Type": "application/json"},
            token=self._controllers.token,
            method="PUT",
        ).text

        result = Model(**json.loads(response_str))
        result.id = model.id  # API update doesn't return id

        return result

    def patch(self, modelId: str, dictAttributes: Dict) -> Model:
        """
        It patches a model (partial update)
        :param modelId: id of the ModelVersion to patch
        :param dictAttributes: attributes to modify
        :return: updated ModelVersion
        """
        if modelId is None:
            raise ValueError("The ModelVersion id is mandatory")
        if dictAttributes is None:
            raise ValueError("dictAttributes is mandatory")

        model = self.get_by_id(modelId)

        if len(dictAttributes) == 0:
            print("Nothing to patch")
        else:
            for key, value in dictAttributes.items():
                model.__setattr__(key, value)

            self.update(model)

        return model

    def delete(
        self,
        model: Model,
        datastorageunitId: int,
        deleteMode: int = None,
        clusterJobParams: ClusterJobParams = None,
    ) -> None:
        """
        It deletes a model
        :param model: a model to delete
        :param datastorageunitId: a datastorageunit to execute delete script
        :param deleteMode: the deletemode
        :param clusterJobParams: clusterJobParams
        :return:
        """
        lst_run_id = self.delete_async(model, datastorageunitId, deleteMode, clusterJobParams)
        for run_id in lst_run_id:
            self.modelversioncontroller.wait_for_job(datastorageunitId, run_id)

    def delete_async(
        self,
        model: Model,
        datastorageunitId: int,
        deleteMode: int = None,
        clusterJobParams: ClusterJobParams = None,
    ) -> List[int]:
        """
        It deletes a model
        :param model: a model to delete
        :param datastorageunitId: a datastorageunit to execute delete script
        :param deleteMode: the deletemode
        :param clusterJobParams: clusterJobParams
        :return:
        """
        if model.id is None:
            raise ValueError("The model id is required")
        if deleteMode is None:
            deleteMode = DeleteMode.Nothing.value

        if clusterJobParams is None:
            url_params = {}
        else:
            url_params = clusterJobParams.__dict__.copy()

        url_params["deleteMode"] = (
            deleteMode if deleteMode is not None else DeleteMode.Nothing.value
        )

        response = get_response(
            url=self._controllers.endpoint + get_url().format(model.id, datastorageunitId),
            params=url_params,
            token=self._controllers.token,
            method="DELETE",
        )
        if response.ok:
            print("Model {} was succesfully deleted".format(model.id))
        else:
            print("There was an error while deleting model {}".format(model.id))

        result = json.loads(response.text)
        return [elem['run_id'] for elem in result]
