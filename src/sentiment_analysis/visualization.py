# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

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
