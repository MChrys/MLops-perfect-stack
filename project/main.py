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

# @hydra.main(config_path="conf", config_name="config")
from hydra import compose, initialize
from omegaconf import OmegaConf


# print(os.environ)
# print(subprocess.run(["ls"]))
import os
import warnings
import sys
from funcy.colls import project
import mlflow
import subprocess


def set_env(cfg: DictConfig) -> None:
    """
    set all env var
    """
    env = cfg["var"]
    for k, v in env.items():
        os.environ[k] = v


initialize(config_path="conf", job_name="gojob")
cfg = compose(config_name="config")
print(OmegaConf.to_yaml(cfg))
traking = cfg["var"]["MLFLOW_TRACKING_URI"]
params = {}
project_path = cfg["project_path"]
experiment = cfg["experiment"]
mlflow.set_tracking_uri(traking)
mlflow.set_experiment(experiment)

# print(subprocess.run(["ls"]))
with mlflow.start_run(nested=True):

    set_env(cfg)

    get_data = mlflow.run(project_path, "process_data", experiment_name=experiment)

    train = mlflow.run(project_path, "train", experiment_name=experiment)

# if __name__ == "__main__":
#    task()
