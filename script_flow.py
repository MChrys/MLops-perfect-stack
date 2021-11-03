from typing import Dict
from prefect import Client, context
import hydra
from omegaconf import DictConfig, OmegaConf
from hydra.core.config_store import ConfigStore
from dataclasses import dataclass


@hydra.main(config_path="project/conf", config_name="config")
def task(cfg: DictConfig):

    # Registering the Config class with the name 'config'.
    client = Client()
    print(OmegaConf.to_yaml(cfg))
    print("-------")
    print(cfg["run"]["flow_id"])
    client.create_flow_run(flow_id=cfg["run"]["flow_id"])


if __name__ == "__main__":
    task()
