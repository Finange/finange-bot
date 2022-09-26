from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)

from app.setup.core import (
    DATA_CLT,
    DEMISSAO_CLT,
    FERIAS_CLT,
    QTD_CLT,
    RENDA,
    SALARIO_CLT,
    cancel,
    clt,
    clt_data,
    clt_demissao,
    clt_ferias,
    clt_quantidade,
    clt_salario,
    inss,
    renda,
)

from app.tax.brazil.impostos import calculo_imposto_de_renda, calculo_inss

# Comando que vai realizar o cálculo do imposto de renda
conv_renda_handler = ConversationHandler(
    entry_points=[CommandHandler('renda', renda)],
    states={
        RENDA: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND, calculo_imposto_de_renda
            )
        ]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# Comando que vai realizar o cálculo da rescisão do CLT
conv_clt_handler = ConversationHandler(
    entry_points=[CommandHandler('clt', clt)],
    states={
        SALARIO_CLT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, clt_salario)
        ],
        QTD_CLT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, clt_quantidade)
        ],
        DATA_CLT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, clt_data)
        ],
        FERIAS_CLT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, clt_ferias)
        ],
        DEMISSAO_CLT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, clt_demissao)
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# Comando que vai realizar o cálculo da contribuição do INSS
conv_inss_handler = ConversationHandler(
    entry_points=[CommandHandler('inss', inss)],
    states={
        RENDA: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, calculo_inss)
        ]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
