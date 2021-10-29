git init
dvc init
git commit -m "Initialize DVC repo"
dvc remote add -d dvc-storage /tmp/dvc-storage
mkdir data

https://github.com/mlflow/mlflow-example.git

dvc add data/wine-quality.csv 
git add data/wine-quality.csv.dvc data/.gitignore

git commit -m 'data: track'


git tag -a 'v1' -m 'raw data'

sed -i '2,1001d' data/wine-quality.csv

git add data/wine-quality.csv.dvc

git commit -m 'data : remove 1000 lines'
git tag -a 'v2'  -m 'removed 1000 lines'
dvc push