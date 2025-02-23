from dominio.playback_interface import PlaybackAbstract
from client import SpotipyClient
from datetime import datetime
from typing import List
class PlaylistPlayback(PlaybackAbstract):   
    def __init__(self):
        super().__init__("playlist")


    def create_playback(self, spotify_client: SpotipyClient, list_tracks: List[str]) -> str:
        playlist_name = str(input("Digite o nome da playlist: ")) #qq coisa fazer um if no proprio main

        if not playlist_name:
            playlist_name = f"Playlist de {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

        public = bool(input("Deseja tornar a playlist pública? (s/n)") == "s")
        random_order = bool(input("Deseja ordem aleatoria? (s/n)") == "s")

        return spotify_client.create_dinamic_playlist(
            playlist_name,
            list_tracks,
            public=public,    
            ordem_aleatoria=random_order
        )

    
    def create_playlist(self):
        pass



