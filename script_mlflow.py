import mlflow
from mlflow import projects
import os
from prefect import Flow
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run
from prefect.run_configs import LocalRun
import prefect
from prefect import task, Flow, Parameter
import subprocess
from prefect import Client

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


@task
def set_uri(traking):
    mlflow.set_tracking_uri(traking)
    return traking


@task
def set_exp(experiment):
    mlflow.set_experiment(experiment)
    return experiment


@task
def run_mlflow(project_path, experiment):
    mlflow.projects.run(
        project_path,
        experiment_name=experiment,
    )


print("experiment setted")
with Flow("gojobflow", run_config=LocalRun()) as flow:
    s = set_uri(traking)
    e = set_exp(experiment)
    r = run_mlflow(project_path, e)
try:
    flow.register(project_name="gojob")
except:
    subprocess.run(["prefect", "create", "project", "gojob"])
    flow.register(project_name="gojob")
