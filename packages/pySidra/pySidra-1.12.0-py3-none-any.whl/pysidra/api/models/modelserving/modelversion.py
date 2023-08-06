import datetime
import enum

from pysidra.api.models.modelserving.model import Model


class ModelVersionStatus(enum.Enum):
    Error = 0
    ModelRegistered = 1
    ImageCreated = 2
    Deploying = 3
    Deployed = 4


class ModelVersion:

    def __init__(
            self,
            idModel: str,
            experimentId: str,
            runId: str,
            id: str = None,
            versionNumber: int = 0,
            metrics: str = None,
            lastTrained: str = datetime.datetime.utcnow().isoformat(),
            imageName: str = None,
            deploymentName: str = None,
            endPoint: str = None,
            status: int = ModelVersionStatus.ModelRegistered.value,
            enabled: bool = False,
            notes: str = None,
            model: Model = None,
    ):
        """

        :param idModel: Id of the model
        :param experimentId: Id of the experiment
        :param runId: Id of the run
        :param versionNumber: Number of the version
        :param metrics: The metrics log to train
        :param lastTrained: DateTime of the last updated model
        :param imageName: Name of the created image
        :param deploymentName: Name of the deployed webservice
        :param endPoint: URL of the endpoint
        :param status: Status of the creation of the model
        :param enabled: Check if the model version is enabled
        :param notes: Store different information
        :param model:
        """
        self.id = id
        self.model = model
        self.idModel = idModel
        self.experimentId = experimentId
        self.runId = runId
        self.versionNumber = versionNumber
        self.metrics = metrics
        self.lastTrained = lastTrained.ljust(27, '0')
        self.imageName = imageName
        self.deploymentName = deploymentName
        self.endPoint = endPoint
        self.status = status
        self.enabled = enabled
        self.notes = notes

    def __repr__(self):
        return self.__dict__.__repr__()

    def __str__(self):
        return str(self.__dict__)
