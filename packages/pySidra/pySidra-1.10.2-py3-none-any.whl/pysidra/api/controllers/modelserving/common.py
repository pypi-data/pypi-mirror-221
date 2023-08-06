import enum
from typing import List


class RunLifeCycleState(enum.Enum):
    PENDING = 0
    RUNNING = 1
    TERMINATING = 2
    TERMINATED = 3
    SKIPPED = 4
    INTERNAL_ERROR = 5


class DatabricksRunResultState(enum.Enum):
    SUCCESS = 0
    FAILED = 1
    TIMEDOUT = 2
    CANCELED = 3


class KeyValueParameter:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class DeleteMode(enum.Enum):
    Nothing = 0
    DeleteRunIfNoMore = 1
    DeleteRunAndExperimentIfNoMore = 2


class ClusterJobParams:
    def __init__(
        self, clusterId: str, timeOutSeconds: int,
    ):
        self.clusterId = clusterId
        self.timeOutSeconds = timeOutSeconds


class ClusterJobDynamicParams(ClusterJobParams):
    def __init__(
        self, parameters: List[KeyValueParameter], clusterId: str, timeOutSeconds: int,
    ):
        super().__init__(clusterId, timeOutSeconds)
        self.parameters = parameters
