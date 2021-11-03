FROM python:3.7.0

RUN pip install mlflow boto3 pymysql
#RUN mkdir /mlflow/

CMD mlflow server \
    --host 0.0.0.0