from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes


async def calculo_imposto_de_renda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.text
    await update.message.reply_text(f"""
    Entendi, então sua renda é {user}
    """)

    return ConversationHandler.END
