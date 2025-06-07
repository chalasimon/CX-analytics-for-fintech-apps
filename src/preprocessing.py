# preprocessing module
import pandas as pd
import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language

class Preprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df

        # Load English model and add language detector
        self.nlp = spacy.load('en_core_web_sm')
        Language.factory("language_detector", func=lambda nlp, name: LanguageDetector())
        self.nlp.add_pipe("language_detector", last=True)

    def remove_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        self.df = self.df.drop_duplicates()
        return self

    def handle_missing_values(self):
        """Handle missing values in the DataFrame."""
        self.df = self.df.dropna(how='any').reset_index(drop=True)
        return self

    def remove_non_english_reviews(self, text_column='review_text'):
        """Filter out non-English reviews."""
        if text_column not in self.df.columns:
            raise ValueError(f"Column '{text_column}' not found in DataFrame")

        def is_english(text):
            try:
                doc = self.nlp(text)
                return doc._.language['language'] == 'en'
            except Exception:
                return False

        self.df = self.df[self.df[text_column].apply(is_english)].reset_index(drop=True)
        return self

    def get_processed_data(self) -> pd.DataFrame:
        """Return the processed DataFrame."""
        return self.df
