import joblib
from azureml.core.model import Model
import numpy as np
import json



def init():
    global model
    # Example when the model is a file
    model_path = Model.get_model_path("apartment_model")
    print("Model Path is  ", model_path)
    model = joblib.load(model_path)


def run(data):
    data = np.array(json.loads(data)['data'])
    y_hat = model.predict(data)
    return json.dumps(y_hat.tolist())