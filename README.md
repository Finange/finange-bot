# Finange Bot

## Como Contribuir

> Antes de continuar a leitura, para ter **acesso à documentação completa** do projeto, **links** dos
> repositórios do Front-End e Back-End (este que você está agora é parte do Back-End, contando
> com o repo da API) e um **passo a passo** para contribuir, você pode acessar os dois links
> abaixo:
>
> [Documentação completa](https://github.com/Finange/finange-documentation#readme)
> \
> [Passo a passo para contribuição](https://github.com/fl1pe/first-contributions/blob/main/translations/README.pt_br.md#primeiras-contribui%C3%A7%C3%B5es)


Primeiro, você vai precisar criar um Bot no seu telegram. Você ver como faz isso <a href="https://help.huggy.io/telegram-bot/como-configurar-o-telegram-bot">aqui</a>!

"Ah, mas por que eu preciso criar um Bot meu, sendo que quero contribuir pro Finange?"! Muito simples! Cada Bot do Telegram funciona por meio de um Token, então, para que você pudesse contribuir diretamente pro Finange, você precisaria ter o Token OFICIAL do Finange, e, por motivos de segurança, isso NÃO é uma opção.

Logo, a forma mais segura de existir esse projeto no formato Open Source é você criar um Bot de simulação, em que você vai rodar o nosso código no seu próprio Bot, testar, ver tudo bonitinho dentro do seu próprio Bot, e, então, você sobe as features/correções para o Finange, entendeu?! Qualquer dúvida, só abrir um <a href="https://github.com/Finange/finange-bot/issues/new/choose"> issue </a> aqui no nosso repositorio que vamos tirar suas dúvidas!

Agora que você já criou seu Bot, você vai precisar adicionar o Token em um arquivo .env. Siga os passos abaixo:

> 1. Crie um arquivo .env no diretório do projeto.
> 2. Adicione a seguinte linha de comando no arquivo.env e cole seu token dentro das aspas:
>
>    ```TOKEN='<seu-token-do-bot>'```
> 3. Agora é só rodar o bot.py


E dessa forma, você já consegue testar todo nosso código dentro da sua máquina, com seu Bot de simulação.

Próxima etapa, você vai instalar o `poetry` na sua máquina usando esse <a href="https://python-poetry.org/docs/">link</a>!

Depois de instalado, você vai rodar o comando `poetry shell` para que seu poetry crie uma máquina virtual para instalar as dependencias do projeto.

Agora, ele vai precisar instalar tais dependências, basta você rodar o comando `poetry install`.

PRONTO! Agora você já pode contribuir com nosso Finange Bot adicionando features ou corrigindo bugs!

Obrigado pela sua contribuição!

## O que preciso saber do código?

Primeiro, você precisa saber que usamos a linguagem de programação <a href="https://www.python.org/">python</a> e é tudo codificado sem usar nenhum tipo de framework.

Porém, usamos uma biblioteca para abstrair os metódos de conexão com o Telegram - que usamos para nosso Bot funcionar. E essa biblioteca é a <a href="https://docs.python-telegram-bot.org/en/stable/telegram.ext.html">python-telegram-bot</a>. Qualquer dúvida sobre os metódos que usamos para fazer o Bot funcionar, basta ler essa documentação no link anterior ou abrir uma <a href="https://github.com/Finange/finange-bot/issues/new/choose">issue </a> no nosso repositorio. Sinta-se a vontade e NÃO precisa ter vergonha.

Toda dúvida é válida!

## Onde entrar em contato e obter ajuda sobre o projeto?

Para contribuir e organizar melhor as implementações do projeto você pode entrar em nosso **grupo
no [Telegram](https://t.me/+cFJ8upuJ5GQzZmE5)**.

> Para entrar no grupo é só clicar no texto "Telegram" acima.

**Todo domingo às 12h (meio dia no horário de Brasília) temos uma call no grupo**, para que
os contribuidores do projeto possam se comunicar e trocar informações.
