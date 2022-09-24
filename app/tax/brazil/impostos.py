from locale import LC_ALL, currency, setlocale

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

setlocale(LC_ALL, 'pt_BR.UTF-8')


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
    Entendi, então sua renda é \
{currency(float(user), grouping=True) if user.isnumeric() else f"{user}"}
    """
    )

    return ConversationHandler.END


async def calculo_inss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Essa função está recebendo a mensagem do usuário a qual foi passada na
    função 'inss'. A função irá retornar o valor para pagamento
    da contribuição que vai diretamente para seu fundo de Previdência Social,
    baseando-se na tabela de contribuição de 2021 (que é a mais recente).
    Futuramente a função não irá retornar somente a tabela do trabalhador CLT,
    mas também de trabalhadores autônomos, MEIs, facultativos, etc.

    Returns:
        int: Essa função vai retornar um inteiro, a qual se refere a uma
        constante que serve para encerrar uma conversa.
    """
    user = update.message.text
    try:
        user = float(user)
    except ValueError:
        await update.message.reply_text(
            f"""
    O valor informado não é válido!
-> /start para ver os comandos de cálculos disponíveis
            """
        )
        return ConversationHandler.END
    porcentual_inss = 0.075
    user_ceil = 7_087.22
    if user <= 1_212.00:
        porcentual_inss = 0.075
    elif 1_212.01 <= user < 2_427.35:
        porcentual_inss = 0.09
    elif 2_427.36 <= user < 3_641.03:
        porcentual_inss = 0.12
    elif user >= 3_641.04:
        porcentual_inss = 0.14
    if user > user_ceil:
        contrib_inss = user_ceil * porcentual_inss
    else:
        contrib_inss = user * porcentual_inss

    await update.message.reply_text(
        f"""
    Entendi, com sua renda de {currency(user, grouping=True)} \
a sua contribuição será de {currency(contrib_inss, grouping=True)}
    """
    )

    return ConversationHandler.END
