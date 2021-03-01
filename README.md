# Cloud linear regression model
> This is a linear regression model that is deployed on azure ML cloud

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#setup)
* [Code Examples](#features)
* [Contact](#contact)

## General info
To have access from everywhere and for our clients to use the model we deploy it on cloud service. This linear regression model is deployed on azure ML cloud 

## Technologies
* Python 3.8.2
* Pandas 1.2.2
* scikit-learn 0.24.1
* seaborn 0.11.1
* matplotlib 3.3.4
* numpy 1.20.1
* azureml-core==1.23.0

## How to run
$ pip install -r requirements.txt
$ python -m nootbook

## Code Examples
Model register

          model = Model.register(workspace = ws,
              model_path ="model/apartment_model.pkl",
              model_name = "apartment_model",
              tags = {"version": "1"},
              description = "Predict apartment price",
              )


## Contact
Created by @cristofor98
