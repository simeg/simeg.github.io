from .scraper import EverdriveScraper
from .state import FileStateTracker
from .notifier import TelegramNotifier


class EverdriveNotifier:
    def __init__(
        self,
        scraper: EverdriveScraper,
        state_tracker: FileStateTracker,
        notifier: TelegramNotifier,
    ):
        self.scraper = scraper
        self.state_tracker = state_tracker
        self.notifier = notifier

    def run(self) -> None:
        current_files = self.scraper.fetch_file_list()
        previous_files = self.state_tracker.load()
        new_files = [f for f in current_files if f not in previous_files]

        if new_files:
            message = "🆕 New EverDrive OS files:\n\n" + "\n".join(
                f"{self.scraper.url}{f}" for f in new_files
            )
            self.notifier.send_telegram_message(message)
            self.state_tracker.save(current_files)
        else:
            print("No new files found.")
