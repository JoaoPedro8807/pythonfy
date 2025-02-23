from dominio.playback_interface import PlaybackAbstract
from typing import List, Any

class Playback:

    def __init__(self, playback: PlaybackAbstract):
        self.playback = playback

    def create_playback(self, spotify_client: Any, list_tracks: List[str]) -> str:
        return self.playback.create_playback(spotify_client, list_tracks)