# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

import os
import warnings
import sys
from funcy.colls import project
import mlflow
import subprocess

traking = "http://localhost:5000"
params = {}
project_path = "."
experiment = "gojob"
mlflow.set_tracking_uri(traking)
mlflow.set_experiment(experiment)

print(subprocess.run(["ls"]))
with mlflow.start_run(nested=True):

    get_data = mlflow.run(project_path, "process_data", experiment_name=experiment)

    train = mlflow.run(project_path, "train", experiment_name=experiment)
