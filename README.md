# Finange Bot

## Como Contribuir

Primeiro, você vai precisar criar um Bot no seu telegram. Você ver como faz isso <a href="https://help.huggy.io/telegram-bot/como-configurar-o-telegram-bot">aqui</a>!

Agora que você já criou seu Bot, vai precisar criar um arquivo na raiz desse projeto chamado `.env`. Pra que? Simples! Lá vai ser o local que você vai guardar informações importantes do projeto, como o TOKEN do Bot - que você recebeu ao criá-lo no Telegram. Para guardar lá, você cria uma variavel chamada `API_TOKEN=<TOKEN>`, substituindo o `<TOKEN>` pelo Token que você recebeu do BotFather. 

Dessa forma, você já consegue testar todo nosso código dentro da sua máquina, com seu Bot de simulação. 

Próxima etapa, você vai instalar o `poetry` na sua máquina usando esse <a href="https://python-poetry.org/docs/">link</a>!

Depois de instalado, você vai rodar o comando `poetry shell` para que seu poetry crie uma máquina virtual para instalar as dependencias do projeto.

Agora, ele vai precisar instalar tais dependências, basta você rodar o comando `poetry install`.

PRONTO! Agora você já pode contribuir com nosso Finange Bot adicionando features ou corrigindo bugs!

Obrigado pela sua contribuição!