import mlflow
from mlflow import projects
import os


import subprocess


# os.environ["AWS_SECRET_ACCESS_KEY"] = "admin1598753"
# os.environ["AWS_ACCESS_KEY_ID"] = "adminminio"
# os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:3001"
# os.environ["MLFLOW_S3_IGNORE_TLS"] = "true"
# os.environ["MLFLOW_TRACKING_URI"] = "localhost:3000"
print("os")
project_path = "./project"
experiment = "gojob"
traking = "http://localhost:5000"
params = {}
import hydra
from omegaconf import DictConfig, OmegaConf


os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["MYSQL_DATABASE"] = "mlflow_database"
os.environ["MYSQL_USER"] = "mlflow_user"
os.environ["MYSQL_PASSWORD"] = "mlflow"
os.environ["MYSQL_ROOT_PASSWORD"] = "mysql"
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"


mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment(experiment)


mlflow.projects.run(
    project_path,
    experiment_name=experiment,
)
