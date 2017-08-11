# megaaaaaaaaaa
# password123
# HvC9eLJz7DbZuc-XZcxTl8WKXxU
# BlL4ObqPdeCFWg

# TODO: reinstall pip, python
# TODO: posts need to be yielded through Subreddit.submissions with start_date = time of last query and end_date = current time
# time of last query must be stored globally

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
        title = unicodedata.normalize('NFKD', post.title).encode('ascii','ignore')
        url = unicodedata.normalize('NFKD', post.url).encode('ascii','ignore')

        if (QUERY in title):
            print(post)
            print(sub)
            print("Title: ", title)
            print("URL: ", url)
            # print("Text: ", truncate(selftext))
            # print("Score: ", post.score)
            print("---------------------------------\n")
