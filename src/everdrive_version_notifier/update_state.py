from pathlib import Path
import json
from bs4 import BeautifulSoup
import requests


class StateUpdater:
    def __init__(self, target_url: str, state_file: Path):
        self.target_url = target_url
        self.state_file = state_file

    def fetch_file_list(self) -> list[str]:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(self.target_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        return sorted(
            link.get("href")
            for link in links
            if link.get("href") and not link.get("href").startswith("?")
        )

    def update_state(self) -> None:
        files = self.fetch_file_list()
        self.state_file.write_text(json.dumps(files, indent=2))
        print(f"Updated {self.state_file} with {len(files)} entries.")


def main():
    updater = StateUpdater(
        "https://krikzz.com/pub/support/everdrive-gb/x-series/OS/",
        Path(__file__).parent / "latest_files.json",
    )
    updater.update_state()


if __name__ == "__main__":
    main()
