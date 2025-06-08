import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict, Counter

class ThematicAnalyzer:
    def __init__(self, max_features=50):
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        self.nlp = spacy.load('en_core_web_sm')
        self.theme_keywords = {
            'login_issues': ['login', 'password', 'authenticate', 'access'],
            'performance': ['slow', 'lag', 'speed', 'loading'],
            'ui_ux': ['interface', 'design', 'layout', 'button'],
            'transactions': ['transfer', 'payment', 'send', 'withdraw'],
            'customer_support': ['support', 'help', 'response', 'service']
        }

    def extract_keywords(self, texts):
        self.vectorizer.fit(texts)
        return self.vectorizer.get_feature_names_out()

    def categorize_keywords(self, keywords):
        theme_counts = defaultdict(int)
        for keyword in keywords:
            found = False
            for theme, words in self.theme_keywords.items():
                if keyword in words:
                    theme_counts[theme] += 1
                    found = True
                    break
            if not found:
                theme_counts['other'] += 1
        return dict(theme_counts)

    def analyze_per_bank(self, df, text_column='processed_review', bank_column='bank_name', top_n=5):
        bank_theme_summary = {}
        for bank in df[bank_column].unique():
            bank_df = df[df[bank_column] == bank]
            keywords = self.extract_keywords(bank_df[text_column].tolist())
            themes = self.categorize_keywords(keywords)
            # Get top N themes
            top_themes = dict(Counter(themes).most_common(top_n))
            bank_theme_summary[bank] = top_themes
        return bank_theme_summary
