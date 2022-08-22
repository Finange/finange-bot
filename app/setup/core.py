import os

class TelegramBot:
    def __init__(self):
        token = os.environ.get('TOKEN')
        self.url_base = f'api.telegram.org/bot{token}/'