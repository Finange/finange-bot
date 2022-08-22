import os
import requests

class TelegramBot:
    def __init__(self):
        token = os.environ.get('TOKEN')
        self.url_base = f'api.telegram.org/bot{token}/'

    def getStartedBot(self):
        update_id = None
    
    def get_messages_from_user(self, update_id):
        link_request = f'{self.url_base}/getUpdates?timeout=100'
    