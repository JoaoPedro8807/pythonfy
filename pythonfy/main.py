from  typing import List, Dict
from client import SpotipyClient
from dotenv import load_dotenv
import os
from exeptions.invalid_param_exeption import InvalidParamException
from dominio.playback import Playback
from dominio.search_types import Search

load_dotenv()

CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
CLIENT_REDIRECT_URI: str = 'http://127.0.0.1:5000/callback'

def main():
    
    sp = SpotipyClient(
        scopes=["modificar_playlist_publica", "modificar_playlist_privada", "modificar_recomendations"],
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_REDIRECT_URI
    )
    while True:
        print("Iniciando Spotipy...")
        SEARCH_TYPE_NAMES = SpotipyClient.get_search_type_names()
        PLAYBACK_TYPES = SpotipyClient.get_playbacks() 

        search_type_option = int(input("Selecione o que você deseja pesquisar: \n\n [1] artist, [2] album, [3] track, [4] playlist, [5] show, [6] episode\n\n"))
        if search_type_option not in range(1, (len(SEARCH_TYPE_NAMES) + 1)):
            raise InvalidParamException("Tipo de playback inválido")

        search_type_name = SEARCH_TYPE_NAMES[search_type_option - 1]
        search_type_instance = Search(SpotipyClient.get_search_type(search_type_name)())
        print("search_type_instance: ", search_type_instance, "search_type_name: ", search_type_name)

        print(f"\n Selecionado {search_type_name.upper()} com sucesso \n")   

        elements_qtde = int(input(f"Digite a quantidade de {search_type_name}`s que deseja ouvir:   (MÁXIMO 10) \n"))

        if elements_qtde <= 0 or elements_qtde > 10:
            raise InvalidParamException("Quantidade de elementos inválida")

        search_types_list: List[str] = []
        for i in range(elements_qtde):
            name = str(input(f"Digite a {i+1}º {search_type_name} que você deseja ouvir: ")).strip()
            if name and name not in search_types_list:
                search_types_list.append(name)

        medias_ids = sp.search_media(search_type_instance, search_types_list)

        playback_type = str(input("Digite o tipo de playback: \n [1] - Criar uma playlist, [2] Criar uma fila\n")).strip()
        if playback_type not in PLAYBACK_TYPES.keys():
            raise InvalidParamException("Tipo de playback inválido")
        
        playback_type = PLAYBACK_TYPES.pop(playback_type)()

        sp.create_playback(playback=Playback(playback_type), list_tracks=medias_ids)

        continuar = input("Deseja criar outra vez? (s/n):  \n").strip()
        if continuar.lower() != 's':
            print("Encerrando o programa...")
            break

if __name__ == '__main__': 
    main()