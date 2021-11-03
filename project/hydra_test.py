from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass


@dataclass
class Run:
    flow_id: str = "None"


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    # pork should be port!
    print(OmegaConf.to_yaml(cfg))
    cs = ConfigStore.instance()
    # Registering the Config class with the name 'config'.
    cs.store(group="run", name="run_1")

    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
