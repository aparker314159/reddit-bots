import praw
import OAuth2Util
import feedparser
from time import sleep
from datetime import datetime

subreddit = "aparkerbotplayground"

def get_feed_entry():
    feed = feedparser.parse("http://read.tomochan.today/rss")
    return feed.entries[0]

user_agent = "A script to post the latest comic from read.tomochan.today by /u/aparker314159"
r = praw.Reddit(user_agent)
o = OAuth2Util.OAuth2Util(r)
o.refresh()
while True:
    hour = datetime.today().hour
    print(hour)
    if hour == 2:
        break
    sleep(3600)
o.refresh()

while True:
    post_title = "Page for " + datetime.today().strftime("%m/%d/%y")
    r.submit(subreddit, post_title, url=get_feed_entry().link, resubmit=True)
    sleep(86400)
    o.refresh()
