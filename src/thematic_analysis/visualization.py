# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


class ThematicVisualizer:
    def __init__(self):
        sns.set(style="whitegrid")

    def plot_wordcloud(self, text_data,color=None):
        # Generate a word cloud image
        wordcloud = WordCloud(width=800, height=400, background_color=color).generate(text_data)

        # Display the generated image:
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Hide axes
        plt.title("Word Cloud of Thematic Analysis", fontsize=16)
        plt.tight_layout()
        plt.show()
    #Visualization of the rating distribution for each bank
    def plot_rating_distribution(self, df, bank_column='bank_name', rating_column='rating'):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=bank_column, y=rating_column, data=df)
        plt.title('Rating Distribution by Bank', fontsize=16)
        plt.xlabel('Bank Name', fontsize=14)
        plt.ylabel('Rating', fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()