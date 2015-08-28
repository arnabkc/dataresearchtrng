__author__ = 'arnab'

import tweepy

# Variables that contains user credentials to access Twitter API
access_token = "404241973-jNrTi1YxGvZxz5jIBbPlPtZQoJO98SXpo8vmboLl"
access_token_Secret = "nOa04gtzrchvHvLikulYeNpP8U70V8Oshj3gomvdEzi1B"
consumer_key = "t1ESYpUz0FbYDshiShx55Ikdj"
consumer_secret= "E2Tpc6S336RMSAkBSaIvbpmKzsCB8vWcvgOiujNN6b5w4IcHLg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_Secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet.text

