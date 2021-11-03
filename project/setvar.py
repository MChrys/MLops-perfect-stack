import hydra
from omegaconf import DictConfig, OmegaConf
import os


@hydra.main(config_path="conf", config_name="config")
def set_env(cfg: DictConfig) -> None:
    """
    set all env var
    """
    env = cfg["var"]
    for k, v in env.items():
        os.environ[k] = v


# print(os.environ)

if __name__ == "__main__":
    set_env()
