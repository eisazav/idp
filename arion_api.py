import requests
from os import environ

user = environ["APIUSER"]
password = environ["APIPASSWORD"]

def get_api_token():
    response = requests.get("https://api.arion.com.co/v1/token", auth=(user, password))
    token = response.json()['token']
    return {"Content-Type":"application/json", "Authorization": f"Bearer {token}"}

def get_files():
    url = "https://api.arion.com.co/v1/files"
    headers = get_api_token()
    response = requests.get(url, headers=headers)
    print(response.status_code)

def get_files_and_text():
    url = "https://api.arion.com.co/v1/files-text"
    headers = get_api_token()
    response = requests.get(url, headers=headers)

def get_text():
    url = "https://api.arion.com.co/v1/text"
    headers = get_api_token()
    response = requests.get(url, headers=headers)
