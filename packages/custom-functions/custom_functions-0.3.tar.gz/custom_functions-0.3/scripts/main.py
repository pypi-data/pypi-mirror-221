import os
import mlflow
import pickle

from custom_functions.ingest_data import ingest_data
from custom_functions.train import train
from custom_functions.score import score

remote_server_uri = "http://localhost:5000"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

exp_name = "Median_housing_value"
mlflow.set_experiment(exp_name)

with mlflow.start_run():
    with mlflow.start_run(nested=True):
        ingest_data()

    with mlflow.start_run(nested=True):
        train()

    with mlflow.start_run(nested=True):
        score()
        
    ARTIFACTS_PATH = "../artifacts"
    os.makedirs(ARTIFACTS_PATH, exist_ok=True)

    PICKLE_PATH = os.path.join(ARTIFACTS_PATH,
                               "param_distribs.pkl").replace("\\", "/")
    with open(PICKLE_PATH, "rb") as file:
        param_distribs = pickle.load(file)

    PICKLE_PATH = os.path.join(ARTIFACTS_PATH,
                               "param_grid.pkl").replace("\\", "/")
    with open(PICKLE_PATH, "rb") as file:
        param_grid = pickle.load(file)

    PICKLE_PATH = os.path.join(ARTIFACTS_PATH,
                               "lin_reg_op.pkl").replace("\\", "/")
    with open(PICKLE_PATH, "rb") as file:
        lin_reg = pickle.load(file)

    PICKLE_PATH = os.path.join(ARTIFACTS_PATH,
                               "tree_reg_op.pkl").replace("\\", "/")
    with open(PICKLE_PATH, "rb") as file:
        tree_reg = pickle.load(file)

    PICKLE_PATH = os.path.join(ARTIFACTS_PATH,
                               "final_rmse.pkl").replace("\\", "/")
    with open(PICKLE_PATH, "rb") as file:
        final_rmse = pickle.load(file)

    mlflow.log_artifact("../datasets/housing/housing.csv")

    mlflow.log_param(key="rnd_search_forest_reg", value=param_distribs)
    mlflow.log_param(key="grid_search_forest_reg", value=param_grid)
    mlflow.log_metrics({"lin_reg_mae": lin_reg[1],
                        "lin_reg_rmse": lin_reg[0]})
    mlflow.log_metric(key="tree_reg_rmse", value=tree_reg)
    mlflow.log_metric(key="final_rmse", value=final_rmse)
    
    print("Save to: {}".format(mlflow.get_artifact_uri()))
