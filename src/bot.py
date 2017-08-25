# TODO: posts need to be yielded through Subreddit.submissions with start_date = time of last query and end_date = current time. Time of last query must be stored globally

import praw
from constants import *

def truncate(text, max_length=75):
    if len(text) > max_length:
        return text[:max_length] + '...'
    else:
        return text

def fetch_posts(subreddits=SUBREDDIT_LIST, query=QUERY):
    reddit = praw.Reddit(SITE_NAME, user_agent=USER_AGENT)
    results, posts, = {}, {}

    for sub in subreddits:
        results[sub] = {}
        # from the beginning of 08/10 until now. See https://www.epochconverter.com/
        for post in reddit.subreddit(sub).submissions(1502323200, 1502423555):
            if (query in post.title):
                results[sub][post.title] = post.url
    return results
    
