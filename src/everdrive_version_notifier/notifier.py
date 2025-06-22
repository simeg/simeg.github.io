import requests


class TelegramNotifier:
    def __init__(self, token: str, chat_id: str, dry_run: bool = False):
        self.token = token
        self.chat_id = chat_id
        self.dry_run = dry_run
        self.telegram_api = "https://api.telegram.org"

    def send_telegram_message(self, message: str) -> None:
        if self.dry_run:
            print("DRY RUN ENABLED — Telegram message would be:\n")
            print(message)
            return

        url = f"{self.telegram_api}/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "disable_web_page_preview": True,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
