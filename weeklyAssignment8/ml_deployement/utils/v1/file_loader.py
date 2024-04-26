import pickle

trained_model_path = 'ml_deployement\datafiles\linear_regression_model.pkl'

# Load the trained model from the pickle file
with open(trained_model_path, 'rb') as f:
    model = pickle.load(f)


   