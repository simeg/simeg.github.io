import os
from pathlib import Path
from dotenv import load_dotenv

from everdrive_version_notifier.scraper import EverdriveScraper
from everdrive_version_notifier.state import FileStateTracker
from everdrive_version_notifier.notifier import TelegramNotifier
from everdrive_version_notifier.coordinator import EverdriveNotifier

# Load environment variables from .env
load_dotenv()

DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"


def main():
    required_env_vars = ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
    missing_vars = [var for var in required_env_vars if os.getenv(var) is None]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    state_file = Path(__file__).parent / "latest_files.json"

    scraper = EverdriveScraper(
        "https://krikzz.com/pub/support/everdrive-gb/x-series/OS/"
    )
    state_tracker = FileStateTracker(state_file)
    notifier = TelegramNotifier(token, chat_id, dry_run=DRY_RUN)
    everdrive_notifier = EverdriveNotifier(scraper, state_tracker, notifier)
    everdrive_notifier.run()


if __name__ == "__main__":
    main()
