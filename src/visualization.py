import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    sentiment_counts = df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()