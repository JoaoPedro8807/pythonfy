import requests
from dominio.spotipy import Spotipy
from dominio.spotipy import ScopeKeys
from typing import Optional, Dict, Any, List
from dominio.spotify_user import SpotifyUser
from dominio.context_uri import Context_uris
import base64   
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
from dominio.playback import Playback
from dominio.search_types import Search
import pprint

 
class SpotipyClient(Spotipy, spotipy.Spotify):
    """
    A spotify client to modify spotify params, like playback, playlists, etc

        @param scopes: List[ScopeKeys]  = get user_token permissions, example: ['modificar_playlist_publica', 'modificar_playlist_privada']

        @param client_id: str
        @param client_secret: str
        @param redirect_uri: str

    """
    __scops: str
    __auth: SpotifyOAuth
    __user: SpotifyUser
    __search_type: Search
    __playback: Playback

    def __init__(self, scopes: List[ScopeKeys] , client_id: str = None, client_secret: str = None, redirect_uri: str = None): # type: ignore
        self.__scops = " ".join(Spotipy.spotify_scopes[scope] for scope in scopes)  
        self.auth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=self.__scops)
        super().__init__(auth_manager=self.auth)
        self.me() # get user infos by default at init

    def me(self) -> Dict[str, Any]:
        me = super().me()
        self.__user=SpotifyUser(
            id=me.get('id', 'undefined'), 
            name=me.get('display_name', 'undefined'), 
            user_url=me.get('external_urls').get('spotify', 'undefined')
        )
        return me
    

    def create_playback(self, playback: Playback, list_tracks: List[str]) -> None:
        
        return playback.create_playback(spotify_client=self, list_tracks=list_tracks)

    def dinamic_queue_by_genre(self, genre: str) -> str:
        pass

    def get_context_uri(self, type_context: Context_uris, id_context: str) -> str:
        return f"spotify:{type_context}:{id_context}"

    def get_artist_id(self, artist_name: str) -> str:
        q = super().search(q=artist_name, type='artist', limit=1, offset=0)
        return q.get("artists").get("items")[0].get("id", "undefined")
    

    def get_top_tracks_by_artist(self, artist_id: str) -> List[str]:
        return [track.get("id", "undefined") for track in super().artist_top_tracks(artist_id).get("tracks")]


    def get_track_id(self, track_name: str) -> str:
        q = super().search(q=track_name, type='track', limit=1, offset=0)
        print("response de ", track_name)
        pprint.pprint(q.get("tracks").get("items")[0])

        return q.get("tracks").get("items")[0].get("id", "undefined")

    def create_dinamic_playlist_by_name(self, playlist_name: str, tracks_names: List[str],  public: bool = True, ordem_aleatoria: bool = False) -> str:
        tracks_ids = [self.get_track_id(track_name) for track_name in tracks_names]
        return self.create_dinamic_playlist(playlist_name, tracks_ids, public, ordem_aleatoria)

    def create_dinamic_playlist(self, playlist_name: str, tracks_ids: List[str],  public: bool = True, random_order: bool = False) -> str:
        print("Criando playlist...")
        if random_order:
            random.shuffle(tracks_ids)

        playlist = super().user_playlist_create(
            self.user_id, name=playlist_name, public=public
        )
        playlist_id = playlist.get("id", "undefined")
        super().playlist_add_items(playlist_id, tracks_ids)

        return playlist_id  

    
    def create_dinamic_queue(self, list_tracks: List[str], random_order: bool = False) -> None:
        print("Criando fila... ")
        if random_order:
            random.shuffle(list_tracks)
        for track_id in list_tracks:
            self.add_to_queue(track_id)

    def search_media(self, search_type: Search, search_list: List[str]) -> List[str]:
        self.__search_type = search_type
        return search_type.search(spotify_client=self, search_list=search_list)


    @property
    def search_type(self) -> Search:
        return self.__search_type
    
    @search_type.setter
    def search_type(self, search_type: Search):
        self.__search_type = search_type

    @property
    def user(self) -> SpotifyUser:
        return self.__user
    
    @user.setter
    def user(self, user: SpotifyUser):
        self.__user = user

    @property
    def user_id(self) -> str:
        return self.__user.id

    @property
    def get_current_scops(self):
        return self.__scops
    
    @property
    def get_auth(self) -> SpotifyOAuth:
        return self.__auth
