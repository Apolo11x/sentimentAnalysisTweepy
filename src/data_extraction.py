import tweepy
import pandas as pd
import os
from textblob import TextBlob
import matplotlib.pyplot as plt
from dotenv import load_dotenv
def authenticate_twitter_app():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_secret_key = os.getenv('API_SECRET_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    
    client = tweepy.Client(bearer_token=api_key)
    return client
def fetch_tweets(client, search_words, year, total_tweets=200):
    query = f"{search_words} lang:es -is:retweet since:{year}-01-01 until:{year}-12-31"
    tweets = client.search_recent_tweets(query=query, max_results=total_tweets, tweet_fields=['created_at', 'text'])
    return tweets
def fetch_tweets(client, search_words, start_date, end_date, total_tweets=200):
    try:
        query = f"{search_words} lang:es -is:retweet"
        tweets = client.search_recent_tweets(query=query, max_results=total_tweets, tweet_fields=['created_at', 'text'])
        #tweets_data = [[tweet.created_at, tweet.text] for tweet in tweets]
        #df = pd.DataFrame(tweets_data, columns=['date', 'text'])

        # Concatenar todos los tweets en un solo texto
        all_tweets_text = " ".join([tweet['text'] for tweet in tweets.data])

        # Analizar el sentimiento del texto concatenado
        analysis = TextBlob(all_tweets_text)
        polarity = analysis.sentiment.polarity

        print(f"Sentiment analysis for '{search_words}' from {start_date} to {end_date}:")
        print(f"Polarity: {polarity}")
    except tw.TweepError as e:
        print(f"Error: {e}")

    
#    tweets = tweepy.Cursor(api.search_tweets, q=company, since=start_date, until=end_date, lang='es').items()
#    tweets_data = [[tweet.created_at, tweet.text] for tweet in tweets]
#    df = pd.DataFrame(tweets_data, columns=['date', 'text'])
#    return df

def save_tweets_to_csv(df, company, start_date, end_date):
    directory = 'data/raw'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = f"{directory}/{company}_{start_date}_to_{end_date}.csv"
def read_companies(file_path):
    with open(file_path, 'r') as file:
        companies = file.read().splitlines()
    return companies

def plot_sentiment(company, polarity):
    plt.figure(figsize=(10, 5))
    plt.bar(company, polarity, color='blue')
    plt.xlabel('Company')
    plt.ylabel('Polarity')
    plt.title('Sentiment Analysis')
    plt.show()

# Example usage
if __name__ == "__main__":
    client = authenticate_twitter_app()
    companies = read_companies('companies.txt')
    year = 2023

    for company in companies:
        df = fetch_tweets(client, company, year)
        save_tweets_to_csv(df, company, f"{year}-01-01", f"{year}-12-31")
        plot_sentiment(company, df['polarity'].mean())
    end_date = "2023-01-31"
    df = fetch_tweets(client, company, start_date, end_date)
    save_tweets_to_csv(df, company, start_date, end_date)

