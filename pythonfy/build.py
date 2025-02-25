import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pythonfy.client import SpotipyClient
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
CLIENT_REDIRECT_URI = 'http://127.0.0.1:5000/callback'
PLAYLIST_URL = 'https://api.spotify.com/v1/users/{CURRENT_USER}/playlists'


def build():
    sp = SpotipyClient(
        scopes=["ler_tocando_agora", "ler_playlists_privadas", "modificar_playback", "modificar_playlist_privada", "modificar_playlist_publica", "recomendations", "ler_biblioteca", "ler_info", "modificar_recomendations"],
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_REDIRECT_URI
    )

    cbjr_id = sp.get_artist_id("Charlie Brown Jr")



    recomend = sp.recommendations(
    )
    print(recomend)

if __name__ == '__main__':
    build() 












