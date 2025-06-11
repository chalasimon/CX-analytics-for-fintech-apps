# Task 1: Data Preparation and Cleaning

This project involves scraping user reviews for selected Ethiopian banking applications from the Google Play Store, cleaning and preprocessing the data, and saving structured datasets for further analysis.

---

## 📦 Project file

task1.ipynb
- This Jupyter notebook contains the code for scraping, cleaning, and preprocessing the data.


---

## 🛠️ Task Workflow

### 1. Web Scraping

Using the `PlayStoreScraper` class from `src/play_store_scraper.py`, we scrape up to **1000 reviews** for each of the following banking apps:

| Bank     | App ID                              |
|----------|-------------------------------------|
| CBE      | `com.combanketh.mobilebanking`      |
| Dashen   | `com.dashen.dashensuperapp`         |
| BOA      | `com.boa.boaMobileBanking`          |

Scraped reviews are saved as `.csv` files in the `data/raw/` directory.

---

### 2. Data Loading

- All CSV files from `data/raw/` are loaded using the `DataLoader` class.
- DataFrames are organized in a dictionary keyed by bank name.
- Summary statistics and column information are printed for inspection.

---

### 3. Preprocessing Steps

Each DataFrame undergoes the following steps via the `Preprocessor` class:

- **Duplicate Removal**
- **Missing Value Handling**
- **Non-English Review Removal** (using spaCy’s `en_core_web_sm` model)

Preprocessed data is saved in `data/processed/` with a separate CSV file for each bank, and a combined file containing all reviews.

---

### 4. Output

After preprocessing, the script prints:

- Summary statistics for each bank’s cleaned data
- Total number of reviews
- Final column names
- Saving the preprocessed data in a combined DataFrame and Postgres database
-  Visualization of the distribution of sentiment trends over time
- Visualization of the rating distribution for each bank
- Word cloud visualization of the most common positive and negative words in reviews
---

## 💾 Output Files

- `data/processed/CBE_preprocessed.csv`
- `data/processed/Dashen_preprocessed.csv`
- `data/processed/BOA_preprocessed.csv`
- `data/processed/combined_preprocessed.csv`
- `data/analyzed/cleaned_review_data.csv`
- `data/analyzed/thematic_analysis_results.csv`
- `src/database/bank_reviews` (Postgres database)

---

## ✅ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
