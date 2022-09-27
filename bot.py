from locale import LC_ALL, setlocale
from os import environ
from sys import exit
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.error import InvalidToken

from app.setup.core import start, text
from app.setup.handlers import (
    conv_clt_handler,
    conv_inss_handler,
    conv_renda_handler,
)

load_dotenv()
#Verifica se o TOKEN existe.
TOKEN = environ.get('TOKEN')
if TOKEN == None:
    exit("Adicione seu TOKEN na variável de ambiente do sistema, ou no arquivo '.env'.\nLeia a documentação para mais detalhes: https://github.com/Finange/finange-bot/blob/main/README.md")


def main() -> None:
    """
    Essa é a principal função, é nela que vamos rodar todas as outras funções
    dependentes, para enfim rodar o bot.
    """

    setlocale(LC_ALL, 'pt_BR.UTF-8')

    # Cria a aplicação e passa pro token do bot
    try:
        app = Application.builder().token(TOKEN).build()
    except InvalidToken:
        exit("Token inválido, utilize um TOKEN passado pelo @BotFather.\nLeia a documentação para mais detalhes: https://github.com/Finange/finange-bot/blob/main/README.md")

    # Comandos

    # Comando para começar o bot
    app.add_handler(CommandHandler('start', start))
    # Comando para adicionar o handler de imposto de renda
    app.add_handler(conv_renda_handler)
    # Comando para adicionar o handler de rescisão da CLT
    app.add_handler(conv_clt_handler)
    # Comando para adicionar o handler da contribuição do INSS
    app.add_handler(conv_inss_handler)
    # Resposta para texto do user
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

    # Começa o bot
    app.run_polling()


if __name__ == '__main__':
    main()
