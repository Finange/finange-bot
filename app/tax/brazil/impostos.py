from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def calculo_imposto_de_renda(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """
    Essa função está recebendo a mensagem do usuário a qual foi passada na
    função 'renda'. Futuramente, nessa função pode ser retornado um cálculo
    com o imposto de renda.

    Return:
        int: Essa função vai retornar um inteiro, a qual se refere a uma
        constante que serve para encerrar uma conversa.
    """
    user = update.message.text
    await update.message.reply_text(
        f"""
    Entendi, então sua renda é {user}
    """
    )

    return ConversationHandler.END
