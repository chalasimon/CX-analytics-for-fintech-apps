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