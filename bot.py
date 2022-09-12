import os

from app.tax.brazil.impostos import calculo_imposto_de_renda
import telegram.ext
from telegram.message import Message

from dotenv import load_dotenv

# Carrega o arquivo .env que contém o Token
load_dotenv()

# Pega o path do Token
API_TOKEN = os.environ.get("API_TOKEN")


def start(update, context) -> Message:
    return update.message.reply_text("""
    Olá, eu sou o Finange, seu Bot Financeiro!

    Sou capaz de calcular seus impostos e organizar sua vida financeira!

    Vamos começar?

    Esses são os impostos que nosso Bot consegue calcular:

    /renda -> Calculo do Imposto de renda
    /clt -> Calculo da rescisão do CLT


    Com esse comando você consegue ver meu poder financeiro:

    /financeiro -> Ajudar você a ser uma pessoa sensata com dinheiro
    """)


def text(update, context) -> Message:
    return update.message.reply_text("""
    Para ver todos os comandos de cálculos clique aqui -> /start
    """)


def main() -> None:
    """Começa o bot"""

    # Atualizador do bot
    updater = telegram.ext.Updater(API_TOKEN, use_context=True)
    disp = updater.dispatcher

    # Comandos
    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler(
        "renda", calculo_imposto_de_renda
        )
    )

    # Texto
    disp.add_handler(telegram.ext.MessageHandler(
        telegram.ext.Filters.text & ~telegram.ext.Filters.command, text))

    # Começa o bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
