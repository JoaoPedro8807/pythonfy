from typing import List, Literal, Optional, Dict, Any
import requests
from dominio.playlist_playback import PlaylistPlayback
from dominio.queue_playback import QueuePlayback
from dominio.playback_interface import PlaybackAbstract
from dominio.search_types import ArtistSearch, TrackSearch, SearchTypeAbstract

ScopeKeys = Literal[
    "modificar_playlist_publica",
    "modificar_playlist_privada",
    "ler_info",
    "ler_email",
    "ler_playback",
    "modificar_playback",
    "ler_tocando_agora",
    "ler_historico",
    "ler_playlists_privadas",
    "ler_playlists_colaborativas",
    "ler_biblioteca",
    "modificar_biblioteca",
    "ler_seguindo",
    "modificar_seguindo",
    "streaming",
    "ler_posicao_podcast",
    "recomendations",
    "modificar_recomendations"
]



class Spotipy:
    """
        Represents my Spotify API
    """

    LOGIN_URL = 'https://accounts.spotify.com/api/token'
    BASE_URL = 'https://api.spotify.com/v1/'


    spotify_scopes = {
    "modificar_playlist_publica": "playlist-modify-public",
    "modificar_playlist_privada": "playlist-modify-private",
    "ler_info": "user-read-private",
    "ler_email": "user-read-email",
    "ler_playback": "user-read-playback-state",
    "modificar_playback": "user-modify-playback-state",
    "ler_tocando_agora": "user-read-currently-playing",
    "ler_historico": "user-read-recently-played",
    "ler_playlists_privadas": "playlist-read-private",
    "ler_playlists_colaborativas": "playlist-read-collaborative",
    "ler_biblioteca": "user-library-read",
    "modificar_biblioteca": "user-library-modify",
    "ler_seguindo": "user-follow-read",
    "modificar_seguindo": "user-follow-modify",
    "streaming": "streaming",
    "ler_posicao_podcast": "user-read-playback-position",
    "recomendations": "user-top-read",
    "modificar_recomendations": "user-follow-modify"
}
    
    ##__search_type_names: List[str] = ['artist', 'album', 'track', 'playlist', 'show', 'episode']

    __search_types: Dict[str, SearchTypeAbstract] = {
            'artist': ArtistSearch,
            'album': 'AlbumSearch', #substituir dps
            'track': TrackSearch,
            'playlist': 'PlaylistSearch',
            'show': 'ShowSearch',
            'episode': 'EpisodeSearch'
        }

    __playbacks: Dict[str, PlaybackAbstract] = {
    '1': PlaylistPlayback,
    '2': QueuePlayback
    }
    
    def make_request(
        self,
        method: str,
        endpoint: str,
        access_token: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Faz uma requisição à API do Spotify.

        Args:
            method: (str)
            endpoint: (str)
            headers: Headers da requisição.
            params: Parâmetros da query string.
            data: Dados do corpo da requisição 
            json: Dados JSON do corpo da requisição.

        Returns:
            Optional:  Resposta da API em formato JSON ou None em caso de erro.
        """

        # Configura os headers padrão com o token de acesso
        default_headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }   
        if headers:
            default_headers.update(headers)

        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=default_headers,
                params=params,
                data=data,
                json=json,
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as http_error:
            print(f"Erro na requisição: {http_error}")
            print(f"Resposta da API: {response.text}")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        
        except Exception as e:
            print(f"Erro: {e}")
            return None
    
    @classmethod
    def get_all_search_types(cls) -> List[Dict[str, SearchTypeAbstract]]:
        return cls.__search_types

    @classmethod
    def get_search_type(cls, search_type: str) -> SearchTypeAbstract:
        return cls.__search_types[search_type]
     

    @classmethod
    def get_search_type_names(cls) -> List[str]:
        return list(cls.__search_types.keys())

    @classmethod
    def get_playbacks(cls) -> Dict[str, PlaybackAbstract]:
        return cls.__playbacks
    

