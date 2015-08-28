__author__ = 'arnab'

# Import necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains user credentials to access Twitter API
access_token = "404241973-jNrTi1YxGvZxz5jIBbPlPtZQoJO98SXpo8vmboLl"
access_token_Secret = "nOa04gtzrchvHvLikulYeNpP8U70V8Oshj3gomvdEzi1B"
api_key = "t1ESYpUz0FbYDshiShx55Ikdj"
api_secret= "E2Tpc6S336RMSAkBSaIvbpmKzsCB8vWcvgOiujNN6b5w4IcHLg"

# This is the basic listener
class StdoutListener(StreamListener):
    def on_data(self, raw_data):
        print raw_data
        return True

    def on_error(self, status_code):
        print status_code


# This handles Twitter authentication and the connection to Twitter Streaming API
l = StdoutListener()

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_Secret)

stream = Stream(auth, l)

# This line filter Twitter Streams to capture data by keywords: 'python, 'javascript', 'ruby'
stream.filter(track=['python', 'javascript', 'ruby'])

