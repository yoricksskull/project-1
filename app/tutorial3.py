# Ysa Pisor
# Radical Software, Fall 2021
# Project 1
# Sept 23, 2021
# python3

import tweepy
import random
import pronouncing
# pronouncing.rhymes("crimes")
# [Grimes,fines,]

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# message = ""

#Option 5: Basic search
# search_resultz = api.search(q="Bezos filter:safe", lang="en", tweet_mode="extended")
# a_very_special_tweet = random.choice(search_resultz)
#print( dir(a_very_special_tweet))
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(a_very_special_tweet._json)

# text = a_very_special_tweet.full_text
# message = text.replace("Bezos", "Bezos, who pays no taxes,")
# print(message)


#Option 6: Mentions
# mentions = api.mentions_timeline()
# mention_tweet = random.choice(mentions)
# thanks = "I'm a radical gratitude bot. Thank you for the mention."
# message = "@" + mention_tweet.user.screen_name + thanks
# print(message)


#Option 7: External API
# mentions = api.mentions_timeline()
# mention_tweet = random.choice(mentions)
# mention_tweet_words = mention_tweet.text.split()
# word = random.choice(mention_tweet_words)
# rhyming_word_list = pronouncing.rhymes(word)
# rhyme_word = random.choice(rhyming_word_list)
#
# template = "You say {}, I say {}."
# message = template.format(word,rhyme_word)
# print(message)

# message = "@" + message
# api.update_status(message, in_reply_to_status_id=mention_tweet.id)
print("Done.")
