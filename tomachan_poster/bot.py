import praw
import OAuth2Util
import feedparser
import requests
import urllib.request
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

subreddit = "aparkerbotplayground"

def get_feed_entry():
    feed = feedparser.parse("http://read.tomochan.today/rss")
    return feed.entries[0]

def get_post_chapter(url):
    htmldoc = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmldoc, "html.parser")
    return soup.find("div", class_="tags").text
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
    post_url = get_feed_entry().link
    post_title = "[DISCUSSION] Tomo-chan wa Onnanoko! Ch. " + get_post_chapter(post_url)
    r.submit(subreddit, post_title, url=post_url, resubmit=True)
    print(post_title)
    print(post_url)
    sleep(86400)
    o.refresh()
