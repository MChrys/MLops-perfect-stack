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
import hydra
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass
from omegaconf import DictConfig, OmegaConf
from hydra.core.config_store import ConfigStore
import yaml

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
def set_env(cfg: DictConfig) -> None:
    """
    set all env var
    """
    env = cfg["var"]
    for k, v in env.items():
        os.environ[k] = v


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
        project_path, experiment_name=experiment,
    )


print("experiment setted")


@dataclass
class Run:
    flow_id: str = "None"


@hydra.main(config_path="project/conf", config_name="config")
def workflow(cfg: DictConfig):
    with Flow("gojobflow", run_config=LocalRun()) as flow:
        logger = prefect.context.get("logger")
        experiment = cfg["experiment"]
        tracking = cfg["var"]["MLFLOW_TRACKING_URI"]
        project_path = cfg["project_path"]

        v = set_env(cfg)
        s = set_uri(tracking)
        e = set_exp(experiment)
        r = run_mlflow(project_path, e)
    try:
        idf = flow.register(project_name="gojob", set_schedule_active=False)
        run_1 = {"flow_id": idf}
        logger.info(cfg["project_path"] + "/conf/run/run_1.yaml")
        with open(cfg["project_path"] + "/conf/run/run_1.yaml", "w+") as outfile:
            yaml.dump(run_1, outfile, default_flow_style=False)
    except:
        subprocess.run(["prefect", "create", "project", "gojob"])
        idf = flow.register(project_name="gojob", set_schedule_active=False)
        run_1 = {"flow_id": idf}
        logger.info(cfg["project_path"] + "/conf/run/run_1.yaml")
        with open(cfg["project_path"] + "/conf/run/run_1.yaml", "w+") as outfile:
            yaml.dump(run_1, outfile, default_flow_style=False)

    # ri = Run(flow_id=idf)
    # Registering the Config class with the name 'config'.
    # cs.store(group="run", name="run_1", node=ri)
    # print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    workflow()
