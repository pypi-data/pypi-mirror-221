from typing import List


class Model:
    def __init__(
        self, name: str, id: str = None, versions: List = None, description: str = None
    ):
        super(Model).__init__()
        self.id = id
        self.name = name
        self.versions = versions
        self.description = description

    def __repr__(self):
        return self.__dict__.__repr__()

    def __str__(self):
        return str(self.__dict__)
