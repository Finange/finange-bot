import requests
import json
import time
import os

while True:
    token = os.environ.get("TOKEN")
    url_base = f'https://api.telegram.org/bot{token}/getUpdates'

    resultado = requests.get(url_base)

    try:
        print(resultado.json())
    except requests.exceptions.ConnectionError:
        print("Error : {}".format(resultado.status_code))
    time.sleep(10) 
