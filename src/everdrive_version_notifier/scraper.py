import requests
from bs4 import BeautifulSoup


class EverdriveScraper:
    def __init__(self, url: str):
        self.url = url

    def fetch_file_list(self) -> list[str]:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        files = [
            link.get("href")
            for link in links
            if link.get("href")
            and not link.get("href").startswith("?")
            and link.get("href").endswith(".zip")
        ]
        return sorted(files)
