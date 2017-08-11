# megaaaaaaaaaa
# password123
# HvC9eLJz7DbZuc-XZcxTl8WKXxU
# BlL4ObqPdeCFWg

# TODO: posts need to be yielded through Subreddit.submissions with start_date = time of last query and end_date = current time. Time of last query must be stored globally

import praw
import unicodedata # For some reason the post attributes are now fetched as type str and not type unicode after switching virtual environments, so we don't need this anymore
from constants import *

def truncate(text, max_length=50):
    if len(text) > max_length:
        return text[:max_length] + '...'
    else:
        return text

reddit = praw.Reddit(SITE_NAME, user_agent=USER_AGENT)
for sub in SUBREDDIT_LIST:
    for post in reddit.subreddit(sub).submissions(1502323200, 1502423555):
        if (QUERY in post.title):
            print(sub)
            print("Title: ", post.title)
            print("URL: ", post.url)
            # print("Text: ", truncate(selftext))
            # print("Score: ", post.score)
            print("---------------------------------\n")
