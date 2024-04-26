
import pickle
import uvicorn
from fastapi import FastAPI

#from mongoengine import connect

#from utils.v1.file_loader import model, scaler
from models.pydantic_models import InputFeatures
#from config.v1.database_config import mongo_config
#from models.mongo_data import InputFeaturesDocument
from utils.v1.preprocessing_features import helper_scale_input_features



# Define FastAPI app
app = FastAPI()

# Load the pickled model
#model = joblib.load("linear_regression_model.pkl")
# Load the pre-trained model from the pickle file
with open("G:\weeklyAssignment\weeklyAssignment8\ml_deployement\linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)


# Endpoint to handle predictions
@app.post("/predict/")
async def predict(features: InputFeatures):
    # Make predictions using the trained model
    prediction = model.predict([[features.bpm, features.danceability, features.valence,
                                  features.energy, features.acousticness, features.instrumentalness,
                                  features.liveness, features.speechiness]])
    prediction = int(prediction[0])

   
    return {'prediction': prediction}

@app.get("/health")
async def health():
    return {"status": "ok"}


# Define MongoDB connection settings
port = 27017
host = "localhost"
db_name = "Customer_personality_prediction_db"

# Connect to MongoDB


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



'''

import uvicorn
from fastapi import FastAPI

from mongoengine import connect

from utils.v1.file_loader import model, scaler
from models.pydantic_models import InputFeatures
from config.v1.database_config import mongo_config
from models.mongo_data import InputFeaturesDocument
from utils.v1.preprocessing_features import helper_scale_input_features

# Define FastAPI app
app = FastAPI()

# Endpoint to handle predictions
@app.post("/predict/")
async def predict(features: InputFeatures):
    # Convert input features to numpy array
    scaled_inputs = helper_scale_input_features([
        features.bpm, features.danceability, features.valence,
        features.energy, features.acousticness, features.instrumentalness,
        features.liveness, features.speechiness
    ])
    
    # Make predictions using the trained model
    prediction = model.predict(scaled_inputs)
    prediction = int(prediction[0])


    # Save input features to MongoDB
    input_features_document = InputFeaturesDocument(
        bpm=features.bpm,
        danceability=features.danceability,
        valence=features.valence,
        energy=features.energy,
        acousticness=features.acousticness,
        instrumentalness=features.instrumentalness,
        liveness=features.liveness,
        speechiness=features.speechiness,
              prediction = prediction
    )
    input_features_document.save()

    return {'prediction': prediction}

@app.get("/health")
async def health():
    return {"status": "ok"}


# Define MongoDB connection settings
port=27017
host="localhost"
db_name="Customer__personality_prediction_db"

# Connect to MongoDB
# connect(db=db_name, host=f'mongodb://{host}:{port}')
connect(db=db_name, host=f'mongodb://{mongo_config.mongo_host}:{port}')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

'''