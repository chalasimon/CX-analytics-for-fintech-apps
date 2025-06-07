import logging
import csv
import os
from datetime import datetime
from google_play_scraper import Sort, reviews

# Ensure the directory exists
DATA_DIR = '../data/raw'
os.makedirs(DATA_DIR, exist_ok=True)

# Configure logging to write in data/raw/scraper.log
logging.basicConfig(
    filename=os.path.join(DATA_DIR, 'scraper.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class PlayStoreScraper:
    def __init__(self, app_id, lang='en', country='us'):
        self.app_id = app_id
        self.lang = lang
        self.country = country

    def get_reviews(self, num_reviews):
        logging.info(f"Fetching reviews for {self.app_id}")
        try:
            result, _ = reviews(
                self.app_id,
                lang=self.lang,
                country=self.country,
                sort=Sort.NEWEST,
                count=num_reviews,
                filter_score_with=None
            )
            logging.info(f"Fetched {len(result)} reviews")
            return result
        except Exception as e:
            logging.error(f"Error fetching reviews: {e}")
            return []

    def save_reviews_to_csv(self, review_data, bank_name):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{bank_name.replace(' ', '_')}_reviews_{timestamp}.csv"
        filepath = os.path.join(DATA_DIR, filename)
        logging.info(f"Saving reviews to {filepath}")

        try:
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
                writer.writeheader()

                for entry in review_data:
                    writer.writerow({
                        'review_text': entry.get('content', ''),
                        'rating': entry.get('score', ''),
                        'date': entry.get('at').strftime('%Y-%m-%d') if entry.get('at') else '',
                        'bank_name': bank_name,
                        'source': 'Google Play'
                    })
            logging.info(f"Successfully saved {len(review_data)} reviews to {filepath}")
        except Exception as e:
            logging.error(f"Error saving reviews to CSV: {e}")