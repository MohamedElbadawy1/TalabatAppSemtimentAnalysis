# scripts/scrape_talabat_reviews.py

from google_play_scraper import reviews, Sort
import pandas as pd
import os

def scrape_talabat_reviews(lang='ar', country='eg', count=10000):
    print(f"Scraping {count} Arabic reviews from Talabat app ({country})...")

    result, _ = reviews(
        'com.talabat',
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=count
    )

    review_list = []
    for r in result:
        review_list.append({
            'userName': r['userName'],
            'content': r['content'],
            'score': r['score'],
            'at': r['at'],
        })

    df = pd.DataFrame(review_list)

    os.makedirs("data/raw", exist_ok=True)

    file_path = f"data/raw/talabat_reviews_{country}_{lang}.csv"
    df.to_csv(file_path, index=False, encoding='utf-8-sig')

    print(f"Saved {len(df)} reviews to {file_path}")
    return df

if __name__ == "__main__":
    df_eg = scrape_talabat_reviews(country='eg')
    df_sa = scrape_talabat_reviews(country='sa')
