import pandas as pd
import numpy as np

# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# from sklearn.linear_model import ElasticNet
import sys
import mlflow
import mlflow.sklearn
import os
import dvc.api
import click


# mlflow.set_experiment("gojob")


path = sys.argv[1] if len(sys.argv) > 1 else 0.5
version = sys.argv[2] if len(sys.argv) > 2 else 0.5
with mlflow.start_run() as mlrun:
    np.random.seed(40)
    repo = os.getcwd()
    data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
    # Read the wine-quality csv file (make sure you're running this from the root of MLflow!)
    data = pd.read_csv(data_url)

    # log data params
    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)
    mlflow.log_param("input_rows", data.shape[0])
    mlflow.log_param("input_cols", data.shape[1])

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    # log artifacts: columns used for modeling
    cols_x = pd.DataFrame(list(train_x.columns))
    cols_x.to_csv("tmp/features.csv", header=False, index=False)
    mlflow.log_artifact("tmp/features.csv")

    cols_y = pd.DataFrame(list(train_y.columns))
    cols_y.to_csv("tmp/targets.csv", header=False, index=False)
    mlflow.log_artifact("tmp/targets.csv")

    train_y.to_csv("tmp/train_y.csv", header=False, index=False)
    mlflow.log_artifact("tmp/train_y.csv")
    test_y.to_csv("tmp/test_y.csv", header=False, index=False)
    mlflow.log_artifact("tmp/test_y.csv")

    train_x.to_csv("tmp/train_x.csv", header=False, index=False)
    mlflow.log_artifact("tmp/train_x.csv")
    test_x.to_csv("tmp/test_x.csv", header=False, index=False)
    mlflow.log_artifact("tmp/test_x.csv")
