from typing import List, TypeVar, Generic

T = TypeVar('T')


class FiltersPaginationResponse(Generic[T]):
    def __init__(self, totalItems: int, items: List[T]):
        """
        :param totalItems: total items returned in items
        :param items: list of items
        """
        self.totalItems = totalItems
        self.items = items


class FiltersPaginationRequest:
    def __init__(
        self,
        skip: int = None,
        take: int = None,
        text: str = None,
        field: str = None,
        sortField: str = None,
        sortDesc: bool = False,
        exactMatch: bool = None,
    ):
        """
        :param skip:
        :param take:
        :param text:
        :param field:
        :param sortField:
        :param sortDesc:
        :param exactMatch:
        """
        self.skip = skip
        self.take = take
        self.text = text
        self.field = field
        self.sortField = sortField
        self.sortDesc = sortDesc
        self.exactMatch = exactMatch
