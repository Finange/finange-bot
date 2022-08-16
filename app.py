import requests
import json
import time
import os

while True:
    token = os.environ.get("TOKEN")
    url_base = f'https://api.telegram.org.bot{token}/getUpdates'

    resultado = requests.get(url_base)

    print(resultado.json())
    time.sleep(10) 