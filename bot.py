# megaaaaaaaaaa
# password123
# HvC9eLJz7DbZuc-XZcxTl8WKXxU
# BlL4ObqPdeCFWg

# TODO: reinstall pip, python

import praw
import unicodedata
from constants import *

def truncate(text, max_length=50):
    if len(text) > max_length:
        return text[:max_length] + '...'
    else:
        return text

# print (BOT)
reddit = praw.Reddit(SITE_NAME, user_agent=USER_AGENT)
for sub in SUBREDDIT_LIST:
    # for post in reddit.subreddit(sub).new(limit=1):
    for post in reddit.subreddit(sub).submissions(1502323200, 1502423555):
        selftext = unicodedata.normalize('NFKD', post.selftext).encode('ascii','ignore')
        print(sub)
        print("Title: ", post.title)
        # print("Text: ", truncate(selftext))
        # print("Score: ", post.score)
        print("---------------------------------\n")
