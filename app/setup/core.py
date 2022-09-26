from locale import currency

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

# Cálculo renda
RENDA = range(1)

# Cálculo INSS
INSS = range(1)

# Rescisão CLT
SALARIO_CLT, QTD_CLT, DATA_CLT, FERIAS_CLT, DEMISSAO_CLT, CALCULO_CLT = range(
    6
)
msg_salario_clt, msg_quantidade_clt, msg_data_clt, msg_demissao_clt = (
    None,
    None,
    None,
    None,
)


# Função para começar o bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Essa função serve para começar o bot, é nela que temos os exemplos de
    outras funções que vão realizar os cálculos.

    Args:
        update: Esse update é o atualizador do bot, é ele que vai enviar as
            mensagens, ou outras informações.
        context: O context praticamente é usado para enviar mensagens e
        realizar diversas tarefas, mas como não estamos usando ele nesse
        projeto, não precisa se preocupar.
    Return:
        Basicamente a função não vai retornar nada, apenas vai enviar a
        mensagem para o usuário através do argumento update.
    """
    await update.message.reply_text(
        """
    Olá, eu sou o Finange, seu Bot Financeiro!

    Sou capaz de calcular seus impostos e organizar sua vida financeira!

    Vamos começar?

    Esses são os impostos que nosso Bot consegue calcular:

    /renda -> Calculo do Imposto de renda
    /clt -> Calculo da rescisão do CLT
    /inss -> Calculo da contribuição do INSS


    Com esse comando você consegue ver meu poder financeiro:

    /financeiro -> Ajudar você a ser uma pessoa sensata com dinheiro
    """
    )


async def renda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Essa função serve para inicializar as outras funções que vão receber
    as mensagens do usuário para assim conseguir realizar o cálculo
    do imposto de renda.

    Return:
        int: Essa função vai retornar um inteiro, que se refere a outra função
        que vai receber o salário do usuário.
    """
    await update.message.reply_text(
        """

    Hmmm! Então você quer que eu calcule seu imposto de renda?

    Ok! Vamos lá.

    Me diga, quanto você ganha?

    Digite /cancel caso queira parar o cálculo.
    """
    )
    return RENDA


# Função para cálculo da contribuição do INSS
async def inss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Essa função serve para inicializar as outras funções que vão receber
    as mensagens do usuário para assim conseguir realizar o cálculo
    de contribuição do INSS.

    Return:
        int: Essa função vai retornar um inteiro, que se refere a outra função
        que vai receber o salário do usuário.
    """
    await update.message.reply_text(
        """

    Ok! Então você deseja que eu calcule sua contribuição ao INSS?

    Ok! Vamos lá.

    Me diga, quanto você ganha?

    Digite /cancel caso queira parar o cálculo.
    """
    )
    return RENDA


# Função para mensagem aleatória do usuário
async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Essa função retorna uma simples mensagem caso o usuário envie
    mensagens aleatórias.

    Return:
        Basicamente a função não vai retornar nada, apenas vai enviar a
        mensagem para o usuário através do argumento update.
    """
    await update.message.reply_text(
        """
    Para ver todos os comandos de cálculos clique aqui -> /start
    """
    )


# Função para parar os cálculos
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Essa função serve para cancelar qualquer cálculo que esteja sendo
    realizado, caso o usuário não queira mais realizar o cálculo.

    Return:
        int: Essa função vai retornar um inteiro, a qual se refere a uma
        constante que serve para encerrar uma conversa.
    """
    await update.message.reply_text(
        """
    Cálculo cancelado!
    """
    )

    return ConversationHandler.END

