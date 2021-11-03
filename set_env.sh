
#install
pip install -r requirements.txt

#droit wait-for-it
chmod +x wait-for-it.sh

#export
export MLFLOW_TRACKING_URI=http://localhost:5000
export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=minio123


#preparation du data DVC
git init
dvc init -f
git commit -m "Initialize DVC repo"
#dvc remote add -d dvc-storage /tmp/dvc-storage
#@mkdir data

#dvc configure artefact minio db
dvc remote add -d minio s3://dvc -f
dvc remote modify minio endpointurl $MLFLOW_S3_ENDPOINT_URL
dvc remote modify minio access_key_id $AWS_ACCESS_KEY_ID
dvc remote modify minio secret_access_key $AWS_SECRET_ACCESS_KEY
#https://github.com/mlflow/mlflow-example.git

dvc add data/wine-quality.csv 
git add data/wine-quality.csv.dvc data/.gitignore

git commit -m 'data: track'


git tag -a 'v1' -m 'raw data'

rm -rf data/wine-quality.csv
rm -rf .dvc/cache

sed -i '2,1001d' data/wine-quality.csv

git add data/wine-quality.csv.dvc

git commit -m 'data : remove 1000 lines'
git tag -a 'v2'  -m 'removed 1000 lines'
dvc push