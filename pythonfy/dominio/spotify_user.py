from pydantic import BaseModel
from typing import Optional
class SpotifyUser(BaseModel):
    id: str
    name: str
    user_url: str

    