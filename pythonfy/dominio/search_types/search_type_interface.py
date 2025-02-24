from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import SpotipyClient

class SearchTypeAbstract(ABC):

    __search_type: str = None

    def __init__(self, search_type: str) -> None:
        self.__search_type = search_type

    @abstractmethod
    def search(self, spotify_client: 'SpotipyClient', search_list: List[str]) -> List[str]:
        pass


    @property
    def search_type(self) -> str:
        return self.__search_type
    
    @search_type.setter
    def search_type(self, search_type: str):
        self.__search_type = search_type