import spotipy
from spotipy.oauth2 import SpotifyOAuth
from myapp import SpotipyClient
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

    calvin_harris = sp.get_artist_id("Calvin Harris")

    top_cbjr = sp.get_top_tracks_by_artist(cbjr_id)
    top_calvin_harris = sp.get_top_tracks_by_artist(calvin_harris)

    top_cbjr.extend(top_calvin_harris)


    playlist_today = sp.create_dinamic_playlist(
        "CBJR e Calvin Harris",
        top_cbjr,
        public=True,
        ordem_aleatoria=True
    )

    sp.start_playback(
        context_uri=sp.get_context_uri("playlist", playlist_today)
    )

if __name__ == '__main__':
    build()

# search = sp.search(
#     "lose yourself",
#     limit=1,
# )

# sp.create_dinamic_playlist_by_name(
#     "outra playlist dinamica",
#     [
#         "wake me up",
#         "lose yourself",
#     ]
# )






# ids_playlists = sp.user_playlists(
#     sp.user_id
# )
#pprint.pprint(ids_playlists)







music_id = '5Z01UMMf7V1o0MzF86s6WJ'

# sp.add_to_queue(
#     uri=sp.get_track_id("wake me up"),
# )




# print(sp.user_id)






