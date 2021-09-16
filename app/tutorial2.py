import tweepy

from authorization_tokens import *

import random

message = ""
# Option 1: Select a message randomly from a list of messages
# phrase_list = ["breaking news:", "a thread:", "my thoughts:"]
# message = random.choice(phrase_list)


# Option 2: A simple Mad Lib
# string_template = "Some people like {} but I like {}."
# word_list = ["rest", "sleep deprivation","ice cream","cake","information","misinformation"]
# word1 = random.choice(word_list)
# word2 = random.choice(word_list)
# message = string_template.format(word1,word2)


# Option 3: A list of possible Mad Libs
# structure = ["My name is {} and I like {}.", "People say I look like {} but only when I'm {}.", "I think {} is the best at {}"]
# word_list1 = ["Owen Wilson","Matthew McConaughey", "Bill Hader"]
# word_list2 = ["saying 'wow'", "saying 'alrightalright'", "saying 'New York's hottest club is"]
# template = random.choice(structure)
# word1 = random.choice(word_list1)
# word2 = random.choice(word_list2)
# message = template.format(word1,word2)


# # Option 4: Using logic to make more intentional choices
string_template = "Hi there, I'm {}, master of {}."
word_list1 = []
word_list2_a = []
word_list2_b = []

# word1 = random.choice(word_list1)
#
# if word1 ==
#     word2 = random.choice(word_list2_a)
# elif word1 ==
#     word2 = random.choice(word_list2_b)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)

print("Done.")
