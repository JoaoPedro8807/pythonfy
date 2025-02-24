from dominio.search_types import SearchTypeAbstract
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from client import SpotipyClient

class Search:

    def __init__(self, search_type: SearchTypeAbstract):
        self.search_type = search_type


    def search(self, spotify_client: 'SpotipyClient', search_list: List[str]) -> List[str]:
        return self.search_type.search(spotify_client, search_list)

