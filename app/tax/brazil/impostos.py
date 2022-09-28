# -*- coding: utf-8 -*-
from locale import currency

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
    salario = update.message.text
    await update.message.reply_text(
        f"""
    Entendi, então sua renda é \
{currency(float(salario), grouping=True) if salario.isnumeric() else f"{salario}"}
    """
    )

    return ConversationHandler.END


async def calculo_clt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Essa função recebe todos os dados de cada state do cálculo CLT e
    realiza o cálculo segundo as condições informadas pelo usuário"""
    try:
        msg_resp = update.message.text.lower()[0]
        if msg_resp != 's' and msg_resp != 'n':
            raise ValueError
    except ValueError:
        await update.message.reply_text(
            f"""
                A reposta não é válida!
            -> /start para ver os comandos de cálculos disponíveis
                        """
        )
        return ConversationHandler.END
    msg_resp = update.message.text

    msg_salario_clt = context.user_data['msg_salario_clt']
    msg_data_inicial = context.user_data['msg_data_inicial']
    msg_data_final = context.user_data['msg_data_final']

    if msg_resp.lower()[0] == 's':
        saldo_salario = (msg_salario_clt / 30) * (int(msg_data_final.strftime('%d')))
        await update.message.reply_text(
            f"""
        {currency(saldo_salario, grouping=True)}

        Finalizamos o seu cálculo.

    -> /start para ver os comandos de cálculos disponíveis
            """
        )
    else:
        if msg_resp.lower()[0] == 'n':
            await update.message.reply_text(
                f"""
                Ok, vamos parar por aqui!

        -> /start para ver os comandos de cálculos disponíveis
                        """
            )
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                f"""
        O valor informado não é válido!
    -> /start para ver os comandos de cálculos disponíveis
                """
            )
            return ConversationHandler.END

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
    contrib = update.message.text  # Contribuição
    try:
        contrib = float(contrib)
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
    if contrib <= 1_212.00:
        porcentual_inss = 0.075
    elif 1_212.01 <= contrib < 2_427.35:
        porcentual_inss = 0.09
    elif 2_427.36 <= contrib < 3_641.03:
        porcentual_inss = 0.12
    elif contrib >= 3_641.04:
        porcentual_inss = 0.14
    if contrib > user_ceil:
        contrib_inss = user_ceil * porcentual_inss
    else:
        contrib_inss = contrib * porcentual_inss

    await update.message.reply_text(
        f"""
    Entendi, com sua renda de {currency(contrib, grouping=True)} \
a sua contribuição será de {currency(contrib_inss, grouping=True)}
    """
    )

    return ConversationHandler.END
