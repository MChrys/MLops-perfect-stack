dvc remote add -d minio s3://bucket-name -f

# add information about storage url (where "https://minio.mysite.com" your url)
dvc remote modify minio endpointurl https://minio.mysite.com

#  add info about login and password
dvc remote modify minio access_key_id my_login
dvc remote modify minio secret_access_key my_password