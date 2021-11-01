import hydra
from omegaconf import DictConfig, OmegaConf
import os


@hydra.main(config_path="conf", config_name="config")
def task(cfg: DictConfig) -> None:
    env = cfg["var"]
    for k, v in env.items():
        os.environ[k] = v


if __name__ == "__main__":
    task()
