from .playback_interface import PlaybackAbstract
from typing import List, TYPE_CHECKING
import random

if TYPE_CHECKING:    
    from client import SpotipyClient

class QueuePlayback(PlaybackAbstract):

    def create_playback(self, spotify_client: 'SpotipyClient', list_tracks: List[str]) -> None:  
        print("Starting Queue playback")
        random_order = bool(input("Deseja ordem aleatoria? (s/n): \n").strip() == "s")
        try:
            spotify_client.create_dinamic_queue(list_tracks, random_order)
            start_now = bool(input("Deseja iniciar a reprodução agora? (s/n): \n").strip() == "s")
            if start_now:
                spotify_client.start_playback()
                print("Executando reprodução...")
                
        except Exception as e:
            print(e)

    def __init__(self):
        super().__init__("queue")

    def __str__(self):
        return self.name
