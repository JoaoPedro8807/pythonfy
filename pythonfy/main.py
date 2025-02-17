from  typing import List
from build import SpotipyClient
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
CLIENT_REDIRECT_URI = 'http://127.0.0.1:5000/callback'
PLAYLIST_URL = 'https://api.spotify.com/v1/users/{CURRENT_USER}/playlists'

def main():
    sp = SpotipyClient(
        scopes=["modificar_playlist_publica", "modificar_playlist_privada", "modificar_recomendations"],
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_REDIRECT_URI
    )
    print("Iniciando Spotipy...")
    artists_names: List[str] = []

    for i in range(3):
        name = str(input("Digite o que quer ouvir: "))
        if name and name not in artists_names:
            artists_names.append(name)

    playlist_name = str(input("Digite o nome da playlist: "))

    random_order = bool(input("Deseja ordem aleatoria? (s/n)") == "s")

    artists_ids: List[str] = []
    for name in artists_names:
        artists_ids.append(sp.get_artist_id(name))

    top_list_tracks: List[str] = []
    for artist_id in artists_ids:
        top_list_tracks.extend(sp.get_top_tracks_by_artist(artist_id))

    playlist_id = sp.create_dinamic_playlist(
        playlist_name,
        top_list_tracks,
        public=True,    
        ordem_aleatoria=random_order
    )

    sp.start_playback(
        context_uri=sp.get_context_uri("playlist", playlist_id)
    )


if __name__ == '__main__':  
    main()