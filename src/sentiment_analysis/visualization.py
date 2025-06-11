# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class SentimentVisualizer:
    def __init__(self):
        sns.set(style="whitegrid")

    def plot_mean_sentiment_trends(self, data):
        # Plotting the mean aggregated sentiment trends
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x="rating", y="mean_sentiment_score", hue="bank_name", marker="o")
        plt.title("Average Sentiment Score by Rating and Bank")
        plt.ylabel("Mean Sentiment Score")
        plt.xlabel("Star Rating")
        plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    def plot_sentiment_distribution(self, data):
        # Count positive and negative reviews per bank
        counts = data.groupby(['bank_name', 'sentiment']).size().reset_index(name='count')
        
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=counts,
            x='bank_name',
            y='count',
            hue='sentiment',
            palette={'POSITIVE': 'green', 'NEGATIVE': 'red'}
        )
        
        plt.title("Number of Positive vs Negative Reviews by Bank", fontsize=16)
        plt.xlabel("Bank Name", fontsize=13)
        plt.ylabel("Number of Reviews", fontsize=13)
        plt.legend(title="Sentiment", title_fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    def plot_sentiment_trends(self, df):
        plt.figure(figsize=(12, 6))
        
        # Ensure date column is datetime
        if not pd.api.types.is_datetime64_any_dtype(df['date']):
            df['date'] = pd.to_datetime(
                df['date'],
                format='mixed',  # New in pandas 2.0+ - handles multiple formats
                errors='coerce',  # Convert problematic dates to NaT instead of failing
                dayfirst=False,   # Set True if dates are DD/MM/YYYY format
                yearfirst=False   # Set True if dates are YYYY/MM/DD format
            )
        monthly = df.groupby([df['date'].dt.to_period('M'), 'bank_name'])['sentiment_score'].mean().unstack()
        monthly.index = monthly.index.to_timestamp()
        
        for bank in monthly.columns:
            plt.plot(monthly.index, monthly[bank], label=bank, marker='o')
        
        plt.title('Sentiment Trends by Bank')
        plt.ylabel('Average Sentiment Score')
        plt.xlabel('Date')
        plt.legend()
        plt.grid(True)
        plt.show()