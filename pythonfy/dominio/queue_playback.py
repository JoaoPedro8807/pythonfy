from .playback_interface import PlaybackAbstract
from typing import List
class QueuePlayback(PlaybackAbstract):

    def create_playback(self, list_tracks: List[str]) -> None:  
        print("Starting Queue playback")

    def __init__(self):
        super().__init__("queue")

    def __str__(self):
        return self.name
