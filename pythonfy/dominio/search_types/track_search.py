from .search_type_interface import SearchTypeAbstract
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import SpotipyClient

class TrackSearch(SearchTypeAbstract):  
    
    def __init__(self):
        super().__init__("track")

    def search(self, spotify_client: 'SpotipyClient', search_list: List[str]) -> List[str]:
        tracks_ids: List[str] = []
        for track_name in search_list:
            track_id = spotify_client.get_track_id(track_name)
            if track_id and track_id not in tracks_ids:
                tracks_ids.append(track_id)
        return tracks_ids