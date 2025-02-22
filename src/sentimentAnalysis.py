import os
import tweepy as tw
from textblob import TextBlob
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#########################################
search_words = "Grupo Nutresa"
date_since = "2021-01-01"
total_tweets = 200
#########################################
try:
    tweets = tw.Cursor(api.search_tweets, q=search_words, lang="es", since=date_since).items(total_tweets)

    # Concatenar todos los tweets en un solo texto
    all_tweets_text = " ".join([tweet.text for tweet in tweets])

    # Analizar el sentimiento del texto concatenado
    analysis = TextBlob(all_tweets_text)
    polarity = analysis.sentiment.polarity

    print(f"Sentiment analysis for '{search_words}' since {date_since}:")
    print(f"Polarity: {polarity}")

except tw.TweepError as e:
    print(f"Error: {e}")

