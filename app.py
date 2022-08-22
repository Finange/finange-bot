import requests
import json
import time
import os

while True:
    TOKEN = os.environ.get("TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    text = "atilio ama dálete"
    url_base = f"https://api.telegram.org/bot5466302728:AAGhs-IYaNzG1ssl518_LJCgKdRM6AvfOCk/getUpdates?timeout=100"

    resultado = requests.get(url_base)

    try:
        print(resultado.json())    
        print(resultado.status_code)
        print(resultado.text)
    except requests.exceptions.ConnectionError:
        print("Error : {}".format(resultado.status_code))
    time.sleep(1) 