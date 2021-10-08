# Ysa Pisor
# Radical Software, Fall 2021
# Project 1
# Oct 8, 2021
# python3

import tweepy
import random

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Access bot
# Select a keyword randomly from a list
search_phrase_list = ["accessibility", "invisible disability", "non-visible disability", "neurodivergent", "neurodiverse", "neurodiversity", "ADHD", "dyslexia", "visual impairment", "ASL interpreter"]
search_phrase = random.choice(search_phrase_list)

# Perform a search with the randomly selected keyword
search_results = api.search(q=search_phrase+" filter:safe", lang="en", tweet_mode="extended")
random_tweet = random.choice(search_results)

# SEND TWEET!!!
tweet_text_a = " Hi! My name is Access Bot. I noticed you might be talking about: "
tweet_text_b = ". I made a collaborative accessibility resource sharing doc that might be useful to you. Would you like to contribute to it? https://docs.google.com/document/d/1PRJsa-0ebTjl39qWWtGBlMsbXi4O-kETdVphBVlSNgA/edit?usp=sharing"
tweet_text_reply = "@" + random_tweet.user.screen_name + tweet_text_a + search_phrase + tweet_text_b
api.update_status(tweet_text_reply, in_reply_to_status_id=random_tweet.id)

print("Done.")
