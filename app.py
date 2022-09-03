import time
import requests
import os 
import telegram

bot = telegram.Bot(token=os.environ.get("TOKEN")) 

bot.sendMessage(chat_id=0000000000, text="Training is done") 

