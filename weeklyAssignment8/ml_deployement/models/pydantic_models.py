from pydantic import BaseModel 



class InputFeatures(BaseModel):
    bpm: float
    danceability: float
    valence: float
    energy: float
    acousticness: float
    instrumentalness: float
    liveness: float
    speechiness: float
