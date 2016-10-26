import praw
import OAuth2Util

subname = "aparkerbotplayground"

r = praw.Reddit(user_agent = "Nintendo Switch Hype Train v0.1 by /u/aparker314159")
o = OAuth2Util.OAuth2Util(r)

while True:
    subreddit = r.get_subreddit(subname)
