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
        # if text is Nan convert to empty string
        texts = [text if isinstance(text, str) else '' for text in texts]
        self.vectorizer.fit(texts)
        return self.vectorizer.get_feature_names_out()

    def categorize_themes(self, text: str) -> list:
        doc = self.nlp(text.lower())
        themes = []
        for token in doc:
            for theme, keywords in self.theme_keywords.items():
                if token.text in keywords and theme not in themes:
                    themes.append(theme)
        return themes if themes else ['other']
    
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

    # extract keywords from the reviews per bank
    def extract_bank_keywords(self, df, text_column='processed_review', bank_column='bank_name'):
        bank_keywords = defaultdict(list)
        for bank in df[bank_column].unique():
            bank_df = df[df[bank_column] == bank]
            keywords = self.extract_keywords(bank_df[text_column].tolist())
            bank_keywords[bank] = keywords
        return bank_keywords