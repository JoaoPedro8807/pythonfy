from dominio.playback_interface import PlaybackAbstract
from datetime import datetime
from typing import List, TYPE_CHECKING
import random

if TYPE_CHECKING:
    from client import SpotipyClient


class PlaylistPlayback(PlaybackAbstract):   
    def __init__(self):
        super().__init__("playlist")


    def create_playback(self, spotify_client: 'SpotipyClient', list_tracks: List[str]) -> str:
        playlist_name = str(input("Digite o nome da playlist: \n")).strip() #qq coisa fazer um if no proprio main

        if not playlist_name:
            playlist_name = f"Playlist de {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

        public = bool(input("Deseja tornar a playlist pública? (s/n)  \n") == "s")
        random_order = bool(input("Deseja ordem aleatoria? (s/n): \n").strip() == "s")

        playlist_id =  spotify_client.create_dinamic_playlist(
            playlist_name,
            list_tracks,
            public=public,    
            random_order=random_order
        )
        start_playback_now = bool(input("Deseja iniciar a reprodução agora? (s/n): \n").strip() == "s")
        if start_playback_now:
            spotify_client.start_playback(
                context_uri=spotify_client.get_context_uri("playlist", playlist_id)
            )
            print("Executando reprodução...")


    
    def create_playlist(self):
        pass



