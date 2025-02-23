from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class PlaybackAbstract(ABC):
    __name: str = None

    def __init__(self, name: str) -> None:
        self.__name = name


    @abstractmethod
    def create_playback(self, list_tracks: List[str]) -> str:
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name