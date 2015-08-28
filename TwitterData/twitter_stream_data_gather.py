__author__ = 'arnab'

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

# Variables that contains user credentials to access Twitter API
access_token = "404241973-jNrTi1YxGvZxz5jIBbPlPtZQoJO98SXpo8vmboLl"
access_token_secret = "nOa04gtzrchvHvLikulYeNpP8U70V8Oshj3gomvdEzi1B"
consumer_key = "t1ESYpUz0FbYDshiShx55Ikdj"
consumer_secret= "E2Tpc6S336RMSAkBSaIvbpmKzsCB8vWcvgOiujNN6b5w4IcHLg"

start_time = time.time() #grabs the system time
keyword_list = ['movie'] #track list

#Listener Class Override
class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit

	def on_data(self, data):

		while (time.time() - self.time) < self.limit:

			try:

				saveFile = open('raw_tweets.json', 'a')
				saveFile.write(data)
				saveFile.write('\n')
				saveFile.close()

				return True


			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		exit()

	def on_error(self, status):

		print status

auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object
