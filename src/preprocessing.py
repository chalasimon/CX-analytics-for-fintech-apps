# preprocessing.py
import pandas as pd
import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language


# Register the language_detector globally if it's not already registered
if "language_detector" not in Language.factories:
    @Language.factory("language_detector")
    def get_lang_detector(nlp, name):
        return LanguageDetector()


class Preprocessor:
    def __init__(self, df: pd.DataFrame):
        if df is None or not isinstance(df, pd.DataFrame):
            raise ValueError("A valid DataFrame must be provided.")

        self.df = df

        # Load spaCy English model
        self.nlp = spacy.load('en_core_web_sm')

        # Add the language_detector to the pipeline if not already present
        if "language_detector" not in self.nlp.pipe_names:
            self.nlp.add_pipe("language_detector", last=True)

    def remove_duplicates(self):
        """Remove duplicate reviews by 'review_text'."""
        self.df = self.df.drop_duplicates(subset='review_text').reset_index(drop=True)
        return self

    def handle_missing_values(self):
        """Remove rows with missing review text, rating, or date."""
        self.df = self.df.dropna(subset=['review_text', 'rating', 'date']).reset_index(drop=True)
        return self

    def remove_non_english_reviews(self, text_column='review_text'):
        """Filter out reviews that are not in English."""
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' not found in DataFrame")

        def is_english(text):
            try:
                doc = self.nlp(text)
                return doc._.language.get('language') == 'en'
            except Exception:
                return False

        self.df = self.df[self.df[text_column].apply(is_english)].reset_index(drop=True)
        return self

    def get_processed_data(self) -> pd.DataFrame:
        """Return the cleaned and filtered DataFrame."""
        return self.df
