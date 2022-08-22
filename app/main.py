from fastapi import FastAPI
import boto3

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{bucket}")
def read_item(bucket: str = None):
    s3 = boto3.resource(
        service_name='s3',
        aws_access_key_id='aaa',
        aws_secret_access_key='bbb',
        endpoint_url='http://localhost:4566',
    )

    my_bucket = s3.Bucket(bucket)

    fileList = []
    for my_bucket_object in my_bucket.objects.all():
        fileList.append(my_bucket_object.key)

    return {"bucket_name": bucket, "items": fileList}