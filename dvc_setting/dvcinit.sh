dvc init -f
git commit -m "Initialize DVC repo"
dvc remote add -d minio s3://dvc
dvc remote modify minio endpointurl http://localhost:9000 

dvc remote modify minio access_key_id minio
dvc remote modify minio secret_access_key minio123

