import os
import requests
import time


class TelegramBot:
    def __init__(self):
        token = os.environ.get("TOKEN")
        self.url_base = f"api.telegram.org/bot{token}/"

    def getStartedBot(self):
        update_id = None

    def get_messages_from_user(self, update_id):
        try:
            link_request = f"{self.url_base}/getUpdates?timeout=100"
        except requests.exceptions.ConnectionError:
            print(f"Error : {self.url_base.status_code}.")
            time.sleep(2)

    def retry_message_response(self, update_id):
        # TODO - Implementar um numero maximo de tentativas de conexão para evitar lentidão no bot
        while self.url_base.status_code != 200:
            if self.url_base.status_code != 404:
                print("Retrying....")
                self.getStartedBot(self)
                self.get_messages_from_user(self, update_id)
                return

            else:
                print(f"Invalid Token: {self.token}")
            time.sleep(4)

            if self.url_base.status_code == 200:
              return 



                
