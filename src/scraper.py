import pandas as pd
import time
from utils import get_soup

BASE_URL = "https://www.bbc.com/news"


def scrape_headlines():
    soup = get_soup(BASE_URL)
    articles = []
    seen = set()

    for item in soup.select("a[href*='/news']"):
        title = item.get_text(strip=True)
        link = item.get("href")

        if not title or not link:
            continue

        if not link.startswith("http"):
            link = "https://www.bbc.com" + link

        if link in seen:
            continue

        seen.add(link)

        articles.append({
            "title": title,
            "link": link
        })

    return articles


def scrape_article_content(article):
    try:
        soup = get_soup(article["link"])
        paragraphs = soup.select("article p")
        content = " ".join([p.get_text() for p in paragraphs])

        article["content"] = content
        article["length"] = len(content)

    except Exception:
        article["content"] = None
        article["length"] = 0

    return article


def run():
    print("Starting scraping pipeline...")

    headlines = scrape_headlines()

    enriched_articles = []

    for article in headlines[:20]:
        enriched_articles.append(scrape_article_content(article))
        time.sleep(1)

    df = pd.DataFrame(enriched_articles)
    df.to_csv("data/raw/news_raw.csv", index=False)

    print("Raw data saved!")


if __name__ == "__main__":
    run()
