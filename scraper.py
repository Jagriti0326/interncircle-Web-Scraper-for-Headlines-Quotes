
import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_JSON = Path("quotes.json")
OUTPUT_TEXT = Path("quotes.txt")


def scrape_quotes():
    quotes_data = []
    page_url = BASE_URL

    while page_url:
        print(f"Scraping: {page_url}")

        try:
            response = requests.get(
                page_url,
                timeout=15,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Request failed: {error}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select(".quote"):
            quote_text = item.select_one(".text").get_text(strip=True)
            author = item.select_one(".author").get_text(strip=True)
            tags = [
                tag.get_text(strip=True)
                for tag in item.select(".tags .tag")
            ]

            quotes_data.append({
                "quote": quote_text,
                "author": author,
                "tags": tags
            })

        next_link = soup.select_one("li.next a")
        if next_link:
            page_url = requests.compat.urljoin(
                page_url, next_link["href"]
            )
            time.sleep(1)
        else:
            page_url = None

    return quotes_data


def save_quotes(quotes):
    with OUTPUT_JSON.open("w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)

    with OUTPUT_TEXT.open("w", encoding="utf-8") as file:
        for number, item in enumerate(quotes, start=1):
            file.write(f"{number}. {item['quote']}\n")
            file.write(f"   Author: {item['author']}\n")
            file.write(f"   Tags: {', '.join(item['tags'])}\n\n")

    print(f"\nSaved {len(quotes)} quotes.")
    print(f"JSON file: {OUTPUT_JSON.resolve()}")
    print(f"Text file: {OUTPUT_TEXT.resolve()}")


def main():
    quotes = scrape_quotes()

    if quotes:
        save_quotes(quotes)
    else:
        print("No quotes were collected. Check your internet connection.")


if __name__ == "__main__":
    main()
