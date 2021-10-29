git init
dvc init
git commit -m "Initialize DVC repo"
dvc remote add -d dvc-storage /tmp/dvc-storage
mkdir data

https://github.com/mlflow/mlflow-example.git

dvc add data/wine-quality.csv 
git add data/wine-quality.csv.dvc data/.gitignore

git commit -m 'data: track'


