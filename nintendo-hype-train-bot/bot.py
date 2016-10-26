import praw
import OAuth2Util
from time import sleep

subname = "askreddit"
finished = set()

r = praw.Reddit(user_agent = "Nintendo Switch Hype Train v0.1 by /u/aparker314159")
o = OAuth2Util.OAuth2Util(r)

while True:
    subreddit = r.get_subreddit(subname)
    comments = subreddit.get_comments(limit=200)
    for c in comments:
        if c in finished:
            break
        print(c.body)
        finished.update([c])
    sleep(1800)
    o.refresh()
