import tweepy as tw 
import pandas as pd# API set-ups for the use of Twitter API
# Insert your keys and tokens belowconsumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth= 
tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweets_list= api.user_timeline(username, count=1, tweet_mode='extended')
 tweet= tweet_list[0]
 print(tweet.full_text)
