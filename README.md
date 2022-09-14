# Finange Bot

## Como Contribuir

Primeiro, você vai precisar criar um Bot no seu telegram. Você ver como faz isso <a href="https://help.huggy.io/telegram-bot/como-configurar-o-telegram-bot">aqui</a>!

"Ah, mas por que eu preciso criar um Bot meu, sendo que quero contribuir pro Finange?"! Muito simples! Cada Bot do Telegram funciona por meio de um Token, então, para que você pudesse contribuir diretamente pro Finange, você precisaria ter o Token OFICIAL do Finange, e, por motivos de segurança, isso NÃO é uma opção.

Logo, a forma mais segura de existir esse projeto no formato Open Source é você criar um Bot de simulação, em que você vai rodar o nosso código no seu próprio Bot, testar, ver tudo bonitinho dentro do seu próprio Bot, e, então, você sobe as features/correções para o Finange, entendeu?! Qualquer dúvida, só abrir um <a href="https://github.com/Finange/finange-bot/issues/new/choose"> issue </a> aqui no nosso repositorio que vamos tirar suas dúvidas!

Agora que você já criou seu Bot, você vai precisar colar o Token no bot.py. Basta procucar a linha que contém este código:
```
app = Application.builder().token("TOKEN").build()
```
Com isso é só substituir o `TOKEN` pelo Token que você recebeu do BotFather.

Dessa forma, você já consegue testar todo nosso código dentro da sua máquina, com seu Bot de simulação. 

Próxima etapa, você vai instalar o `poetry` na sua máquina usando esse <a href="https://python-poetry.org/docs/">link</a>!

Depois de instalado, você vai rodar o comando `poetry shell` para que seu poetry crie uma máquina virtual para instalar as dependencias do projeto.

Agora, ele vai precisar instalar tais dependências, basta você rodar o comando `poetry install`.

PRONTO! Agora você já pode contribuir com nosso Finange Bot adicionando features ou corrigindo bugs!

Obrigado pela sua contribuição!

## O que preciso saber do código?

Primeiro, você precisa saber que usamos a linguagem de programação <a href="https://www.python.org/">python</a> e é tudo codificado sem usar nenhum tipo de framework.

Porém, usamos uma biblioteca para abstrair os metódos de conexão com o Telegram - que usamos para nosso Bot funcionar. E essa biblioteca é a <a href="https://docs.python-telegram-bot.org/en/stable/telegram.ext.html">python-telegram-bot</a>. Qualquer dúvida sobre os metódos que usamos para fazer o Bot funcionar, basta ler essa documentação no link anterior ou abrir uma <a href="https://github.com/Finange/finange-bot/issues/new/choose">issue </a> no nosso repositorio. Sinta-se a vontade e NÃO precisa ter vergonha.

Toda dúvida é válida!
