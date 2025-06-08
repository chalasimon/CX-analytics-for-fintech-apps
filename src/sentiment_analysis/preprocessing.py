#import dependencies
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Tokenize the text
        tokens = word_tokenize(text.lower())
        # Remove stop words and non-alphabetic tokens
        stopwords = set(stopwords.words('english'))
        tokens = [word for word in tokens if word.isalnum() and word not in stopwords]
        # Lemmatize the tokens
        lemmatized_tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        return ' '.join(lemmatized_tokens)

    def preprocess_dataframe(self, df, text_column):
        df['processed_review'] = df[text_column].apply(self.preprocess_text)
        return df