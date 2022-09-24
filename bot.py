from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from app.setup.core import (
    RENDA,
    SALARIO_CLT,
    QTD_CLT,
    DATA_CLT,
    FERIAS_CLT,
    DEMISSAO_CLT,
    cancel,
    renda,
    start,
    text,
    clt,
    clt_salario,
    clt_quantidade,
    clt_data,
    clt_ferias,
    clt_demissao,
)
from app.tax.brazil.impostos import calculo_imposto_de_renda


def main() -> None:
    """
    Essa é a principal função, é nela que vamos rodar todas as outras funções
    dependentes, para enfim rodar o bot.
    """

    # Cria a aplicação e passa pro token do bot
    app = (
        Application.builder()
        .token('TOKEN')
        .build()
    )

    # Comandos

    # Comando para começar o bot
    app.add_handler(CommandHandler('start', start))

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
    app.add_handler(conv_renda_handler)

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
    app.add_handler(conv_clt_handler)

    # Resposta para texto do user
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

    # Começa o bot
    app.run_polling()


if __name__ == '__main__':
    main()
