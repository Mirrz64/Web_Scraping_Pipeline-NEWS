import requests
from bs4 import BeautifulSoup


def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-GB,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        if not response.text.strip():
            print(f"Empty response from {url}")
            return None

        return BeautifulSoup(response.text, "lxml")

    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return None