from .search_type_interface import SearchTypeAbstract
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import SpotipyClient


class ArtistSearch(SearchTypeAbstract):

    def __init__(self):
        super().__init__("artist")

    def search(self, spotify_client: 'SpotipyClient', search_list: List[str]) -> List[str]:
        artists_ids: List[str] = [spotify_client.get_artist_id(artist_name=artist_name) for artist_name in search_list]
        top_list_tracks: List[str] = []
        for artist_id in artists_ids:
            top_list_tracks.extend(spotify_client.get_top_tracks_by_artist(artist_id))
            
        return top_list_tracks