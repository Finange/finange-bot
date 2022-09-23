from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from app.setup.core import RENDA, cancel, renda, start, text
from app.tax.brazil.impostos import calculo_imposto_de_renda


def main() -> None:
    """
    Essa é a principal função, é nela que vamos rodar todas as outras funções
    dependentes, para enfim rodar o bot.
    """

    # Cria a aplicação e passa pro token do bot
    app = Application.builder().token("TOKEN").build()

    # Comandos
    app.add_handler(CommandHandler('start', start))

    conv_handler = ConversationHandler(
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
    app.add_handler(conv_handler)

    # Resposta para texto do user
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

    # Começa o bot
    app.run_polling()


if __name__ == '__main__':
    main()
