# import necessary libraries
from transformers import pipeline
import pandas as pd

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, texts):
        results = self.sentiment_pipeline(texts)
        return results
    
