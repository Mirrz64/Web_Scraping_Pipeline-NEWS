import pandas as pd
import os


def clean_data():
    path = "data/raw/news_raw.csv"

    if not os.path.exists(path):
        print("Raw file not found. Run scraper first.")
        return

    if os.stat(path).st_size == 0:
        print("Raw file is empty. Scraper likely failed.")
        return

    df = pd.read_csv(path)

    if df.empty:
        print("DataFrame is empty. Nothing to clean.")
        return

    print(f"Loaded {len(df)} rows. Cleaning dataset...")

    df = df.dropna(subset=["content"])
    df = df.drop_duplicates(subset=["title"])
    df = df[df["length"] > 200]

    df["content"] = df["content"].str.replace("\n", " ", regex=True)
    df["word_count"] = df["content"].apply(lambda x: len(x.split()))

    print(f"Remaining after cleaning: {len(df)} rows")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/news_cleaned.csv", index=False)

    print("Processed data saved!")


if __name__ == "__main__":
    clean_data()