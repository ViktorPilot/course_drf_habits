import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(chat_id, message):
    """Метод отправляет через телеграм-бота сообщение о начале выполнения привычки"""
    params = {"text": message,
              "chat_id": chat_id}
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
