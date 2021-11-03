from io import BytesIO

import pandas as pd
from minio import Minio

doc = {
    "AWS_ACCESS_KEY_ID": "minio",
    "AWS_SECRET_ACCESS_KEY": "minio123",
    "MYSQL_DATABASE": "mlflow_database",
    "MYSQL_USER": "mlflow_user",
    "MYSQL_PASSWORD": "mlflow",
    "MYSQL_ROOT_PASSWORD": "mysql",
    "MLFLOW_TRACKING_URI": "http://localhost:5000",
    "MLFLOW_S3_ENDPOINT_URL": "http://localhost:9000",
}
minioClient = Minio(
    "localhost:9000",
    access_key=doc["AWS_ACCESS_KEY_ID"],
    secret_key=doc["AWS_SECRET_ACCESS_KEY"],
    secure=False,
)

df = pd.DataFrame()
csv_bytes = df.to_csv().encode("utf-8")
csv_buffer = BytesIO(csv_bytes)

minioClient.put_object(
    "dvc",
    "wine-quality.csv",
    data=csv_buffer,
    length=len(csv_bytes),
    content_type="application/csv",
)
