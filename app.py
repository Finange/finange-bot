import time
import requests
import os 
import telegram.ext

API_TOKEN = os.environ.get("API_TOKEN")

def start(update, context):
    update.message.reply_text("Hey! Como posso ajudar você?")

updater = telegram.ext.Updater(API_TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()