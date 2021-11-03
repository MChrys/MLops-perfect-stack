# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

import os
import warnings
import sys
import mlflow
import subprocess

# traking = "http://localhost:5000"

# os.environ["AWS_ACCESS_KEY_ID"] = "minio"
# os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
# os.environ["MYSQL_DATABASE"] = "mlflow_database"
# os.environ["MYSQL_USER"] = "mlflow_user"
# os.environ["MYSQL_PASSWORD"] = "mlflow"
# os.environ["MYSQL_ROOT_PASSWORD"] = "mysql"
# os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
# os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
import hydra
from omegaconf import DictConfig, OmegaConf
import os

import uuid


def set_env(cfg: DictConfig) -> None:
    """
    set all env var
    """
    env = cfg["var"]
    for k, v in env.items():
        os.environ[k] = v

<<<<<<< Updated upstream

# @hydra.main(config_path="conf", config_name="config")
from hydra import compose, initialize
from omegaconf import OmegaConf

traking = "http://localhost:5000"
params = {}
project_path = "."
experiment = "gojob"
mlflow.set_tracking_uri(traking)
mlflow.set_experiment(experiment)

print(subprocess.run(["ls"]))
with mlflow.start_run(nested=True):

    get_data = mlflow.run(project_path, "process_data", experiment_name=experiment)

    train = mlflow.run(project_path, "train", experiment_name=experiment)
=======

# @hydra.main(config_path="conf", config_name="config")
from hydra import compose, initialize
from omegaconf import OmegaConf

initialize(config_path="conf", job_name="test_app")
cfg = compose(config_name="config")
print(OmegaConf.to_yaml(cfg))
params = {}

# print(os.environ)
# print(subprocess.run(["ls"]))
run_id = str(uuid.uuid4())
print("workflow")
print(run_id)

# os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
with mlflow.start_run(nested=True):
    project_path = cfg["project_path"]
    experiment = cfg["experiment"]
    mlflow.set_experiment(experiment)
    os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
    mlflow.set_tracking_uri(cfg["var"]["MLFLOW_TRACKING_URI"])

    print(cfg["var"]["MLFLOW_TRACKING_URI"])

    # set_env = mlflow.run(project_path, "env", experiment_name=experiment)
    set_env(cfg)
    # print(os.environ)
    get_data = mlflow.run(project_path, "process_data", experiment_name=experiment)
    print("=================>")
    print("get_data success")
    train = mlflow.run(project_path, "train", experiment_name=experiment)
    print("=================>")
    print("train success")
    print(OmegaConf.to_yaml(DictConfig(dict(os.environ))))
    mlflow.end_run()
>>>>>>> Stashed changes


# if __name__ == "__main__":
#    task()
