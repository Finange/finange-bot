from app.tax.brazil.impostos import calculo_imposto_de_renda
from telegram.ext import Application, CommandHandler, \
 MessageHandler, ContextTypes, filters, ConversationHandler
from telegram import Update

RENDA = range(1)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    Olá, eu sou o Finange, seu Bot Financeiro!

    Sou capaz de calcular seus impostos e organizar sua vida financeira!

    Vamos começar?

    Esses são os impostos que nosso Bot consegue calcular:

    /renda -> Calculo do Imposto de renda
    /clt -> Calculo da rescisão do CLT


    Com esse comando você consegue ver meu poder financeiro:

    /financeiro -> Ajudar você a ser uma pessoa sensata com dinheiro
    """)


async def renda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("""

    Hmmm! Então você quer que eu calcule seu imposto de renda?

    Ok! Vamos lá.

    Me diga, quanto você ganha?

    Digite /cancel caso queira parar o cálculo.
    """)
    return RENDA


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    Para ver todos os comandos de cálculos clique aqui -> /start
    """)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    Cálculo de renda cancelado!
    """)

    return ConversationHandler.END


def main() -> None:
    """Começa o bot"""

    # Cria a aplicação e passa pro token do bot
    app = Application.builder().token("TOKEN").build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("renda", renda)],
        states={
            RENDA: [MessageHandler(filters.TEXT & ~filters.COMMAND, calculo_imposto_de_renda)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)

    # Resposta para texto do user
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

    # Começa o bot
    app.run_polling()


if __name__ == "__main__":
    main()
