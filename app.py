import time
import requests
import os 
import telegram.ext

API_TOKEN = os.environ.get("API_TOKEN")

def start(update, context):
    update.message.reply_text("""
    Olá, eu sou o Finange, seu Bot Financeiro! 

    Sou capaz de calcular seus impostos e organizar sua vida financeira!

    Vamos começar?
    
    Esses são os impostos que nosso Bot consegue calcular:

    /renda -> Calculo do Imposto de renda
    /clt -> Calculo da rescisão do CLT
    

    Com esse comando você consegue ver meu poder financeiro:

    /financeiro -> Ajudar você a ser uma pessoa sensata com dinheiro
    """)


updater = telegram.ext.Updater(API_TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()