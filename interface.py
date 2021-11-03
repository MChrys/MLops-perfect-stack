import yaml
import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass
import os
from os import listdir
from os.path import isfile, join


def task():
    run_1 = {"flow_id": "test"}
    current_path = os.getcwd()
    project_path = current_path + "/project"
    print(project_path)
    print("/home/chrysostome/Desktop/test_gojob/gojob/project/conf/config.yaml")
    print(project_path + "/conf/config.yaml")
    with open(project_path + "/conf/config.yaml", "r") as outfile:
        config = yaml.load(outfile, Loader=yaml.FullLoader)
    print(config)
    with open(project_path + "/conf/config.yaml", "w") as outfile:
        config["repo"] = current_path
        config["project_path"] = project_path
        documents = yaml.dump(config, outfile)

    onlyfiles = [
        f
        for f in listdir(project_path + "/conf/data")
        if isfile(join(project_path + "/conf/data", f))
    ]
    print(onlyfiles)
    for f in onlyfiles:
        with open(project_path + "/conf/data/{}".format(f), "r") as outfile:
            config = yaml.load(outfile, Loader=yaml.FullLoader)
        print(config)
        with open(project_path + "/conf/data/{}".format(f), "w") as outfile:
            config["path"] = current_path + "/data/" + config["name"]
            # config["project_path"] = project_path
            documents = yaml.dump(config, outfile)


task()
