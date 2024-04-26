from mongoengine import Document, FloatField,StringField

class InputFeaturesDocument(Document):
    bpm = FloatField(required=True)
    danceability = FloatField(required=True)
    valence = FloatField(required=True)
    energy = FloatField(required=True)
    acousticness = FloatField(required=True)
    instrumentalness = FloatField(required=True)
    liveness = FloatField(required=True)
    speechiness = FloatField(required=True)
    prediction = StringField()
