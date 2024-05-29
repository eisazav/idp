from os import environ
from google.cloud import storage
from uuid import uuid4

project_id = 'pokenea1'
bucket_name = 'arion_files'
environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'gcp_credentials.json'

client = storage.Client(project_id)

def upload_file(file):

    bucket_file = f'{uuid4().hex}.pdf'

    bucket = client.get_bucket(bucket_name)

    blob = bucket.blob(bucket_file)

    blob.upload_from_file(file)

    url = f"https://storage.googleapis.com/arion_files/{bucket_file}"

    return url
