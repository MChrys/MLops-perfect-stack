from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf


@dataclass
class MySQLConfig:
    host: str = "localhost"
    port: int = 3306


cs = ConfigStore.instance()
instance = MySQLConfig(port=4501)
# Registering the Config class with the name 'config'.
cs.store(group="run", name="run1", node=instance)


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: MySQLConfig) -> None:
    # pork should be port!
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
