from msg import GetMessages

bot = GetMessages()


def calculo_imposto_de_renda(update, context):
    update.message.reply_text("""

    Hmmm! Então você quer que eu calcule seu imposto de renda?

    Ok! Vamos lá.

    Me diga, quanto você ganha?

    """)

    calcula()


def calcula():
    bot.iniciar()
