from  typing import List, Dict
from client import SpotipyClient
from dotenv import load_dotenv
import os
from exeptions.invalid_param_exeption import InvalidParamException
from dominio.queue_playback import QueuePlayback
from dominio.playlist_playback import PlaylistPlayback
from dominio.playback import Playback
from dominio.playback_interface import PlaybackAbstract

load_dotenv()

CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
CLIENT_REDIRECT_URI: str = 'http://127.0.0.1:5000/callback'
PLAYLIST_URL: str = 'https://api.spotify.com/v1/users/{CURRENT_USER}/playlists'
SEARCH_TYPE: List[str] = ['artist', 'album', 'track', 'playlist', 'show', 'episode']
PLAYBACK_TYPE: Dict[str, PlaybackAbstract] = {
    '1': PlaylistPlayback,
    '2': QueuePlayback
}

def main():
    
    sp = SpotipyClient(
        scopes=["modificar_playlist_publica", "modificar_playlist_privada", "modificar_recomendations"],
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_REDIRECT_URI
    )
    while True:
        print("Iniciando Spotipy...")

        search_types_list: List[str] = []

        search_type = int(input("Digite o que deseja ouvir: \n\n [1] artist, [2] album, [3] track, [4] playlist, [5] show, [6] episode\n\n"))
        if search_type not in range(1, (len(SEARCH_TYPE) + 1)):
            raise InvalidParamException("Tipo de playback inválido")

        search_type = SEARCH_TYPE[search_type - 1]

        print(f"\n Selecionado {search_type.upper()} com sucesso \n")
        
        playback_type = str(input("Digite o tipo de playback: \n [1] - Criar uma playlist, [2] Criar uma fila\n")).strip()
        if playback_type not in PLAYBACK_TYPE.keys():
            raise InvalidParamException("Tipo de playback inválido")
        
        playback_type = PLAYBACK_TYPE.pop(playback_type)()

        #normalizar no abstract'

        elements_qtde = int(input(f"Digite a quantidade de {search_type}`s que deseja ouvir:   (MÁXIMO 10)"))

        if elements_qtde <= 0 or elements_qtde > 10:
            raise InvalidParamException("Quantidade de elementos inválida")

        for i in range(elements_qtde):
            name = str(input(f"Digite a {i+1}º {search_type} que você deseja ouvir: ")).strip()
            if name and name not in search_types_list:
                search_types_list.append(name)


        random_order = bool(input("Deseja ordem aleatoria? (s/n)") == "s")

        media_to_play_ids: List[str] = [] # media = artist, album, track etc

        for name in search_types_list:
            artist_id = sp.get_artist_id(name)
            if artist_id:
                media_to_play_ids.append(artist_id)

        top_list_tracks: List[str] = []

        for media_id in media_to_play_ids:
            top_list_tracks.extend(sp.get_top_tracks_by_artist(media_id))

        playback  = sp.create_playback(playback=Playback(playback_type), list_tracks=top_list_tracks) #playlist_id

        sp.start_playback(
            context_uri=sp.get_context_uri(playback_type.name, playback)
        )


        continuar = input("Deseja criar outra playlist? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando o programa...")
            break

if __name__ == '__main__':  
    main()