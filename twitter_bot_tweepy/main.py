import tweepy
import tkinter
import time

access_token = "1314825718140825600-ljurV2RvTPnfJCjYheruDkecaYwq3y"
access_token_secret = "a4GxnvoDS6PhyLFre5JZZCA6ACJpN3UnlInZdHdCdByjD"
consumer_key = "dpLxZPS50Oldmri5Hrn2uj2y2"
consumer_secret = "fvLJ7W4uy7tg4D41mnHGndht7W6J9PxsRCBdfrx2ESaGuBCJTY"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# # Define the search query and the number of tweets to retrieve
# search_query = "#100DaysOfCode"
# num_tweets = 5

# # Retrieve tweets
# tweets = api.search_tweets(q=search_query, count=num_tweets)

user = api.verify_credentials()
print(user)