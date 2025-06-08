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