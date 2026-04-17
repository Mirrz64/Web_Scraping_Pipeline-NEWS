# Web Scraping Pipeline - BBC News

## Overview
This project extracts news articles from BBC News, processes them, and prepares structured data for analysis.

## Pipeline Steps
1. Scraping headlines and article content
2. Cleaning and filtering text
3. Saving structured datasets
4. Performing exploratory analysis

## Tools Used
- Python
- BeautifulSoup
- Pandas
- Matplotlib
- Seaborn

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run scraper:
   python src/scraper.py

3. Run cleaner:
   python src/cleaner.py

4. Open notebook:
   notebooks/analysis.ipynb

## Output
- Raw dataset (data/raw)
- Cleaned dataset (data/processed)
- Visual insights in notebook