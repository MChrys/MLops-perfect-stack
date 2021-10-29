import mlflow
from mlflow import projects
import os

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
mlflow.set_tracking_uri(traking)

mlflow.set_experiment(experiment)
print("experiment setted")
mlflow.projects.run(
    project_path,
    experiment_name=experiment,
)
