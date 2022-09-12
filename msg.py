import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")


class GetMessages:

    def __init__(self) -> None:
        self.url_api = f'https://api.telegram.org/bot{API_TOKEN}/'

    def iniciar(self) -> None:
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']

            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']

    def obter_mensagens(self, update_id) -> None:
        url_requisicao = f'{self.url_api}getUpdates?timeout=100'

        if update_id:
            url_requisicao = f'{url_requisicao}&offset={update_id + 1}'

        resultado = requests.get(url_requisicao)
        return json.loads(resultado.content)

    def calcular(self):
        return f'calculando {self.obter_mensagens()}'

    def resposta(self, chat_id) -> None:
        url_envio = f'{self.url_api}sendMessage?chat_id={chat_id}&text={self.calcular()}'
        requests.get(url_envio)
