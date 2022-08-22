import requests
import json
import time
import os

from .app.setup.core import TelegramBot

while True:
    TOKEN = os.environ.get("TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    text = "atilio ama dálete"
    url_base = f"https://api.telegram.org/bot5466302728:AAGhs-IYaNzG1ssl518_LJCgKdRM6AvfOCk/getUpdates"

    bot = TelegramBot

    try:
        print(bot.see_information(url_base))
    except requests.exceptions.ConnectionError:
        print(f'deu')
    time.sleep(1) 