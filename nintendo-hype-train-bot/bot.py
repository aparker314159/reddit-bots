import praw
import OAuth2Util
from time import sleep

subname = "aparkerbotplayground"
finished = set()

r = praw.Reddit(user_agent = "Nintendo Switch Hype Train v0.1 by /u/aparker314159")
o = OAuth2Util.OAuth2Util(r)

onboard = 0

while True:
    subreddit = r.get_subreddit(subname)
    comments = subreddit.get_comments(limit=200)
    for c in comments:
        if c in finished:
            break
        onboard = onboard + 1
        message = """
        #ALL ABOARD THE SWITCH HYPE TRAIN!
        #[CHOO CHOO!](http://imgur.com/y9igYes)
        """ + str(onboard) + """people onboard the hype train!

        ^________________________________

        ^This ^is ^a ^bot, ^and ^this ^action ^was ^performed ^automatically. ^Please ^contact ^/u/aparker314159 ^for ^any ^questions ^or ^comments.
        """
        c.reply(message)
        finished.update([c])
    sleep(900)
    o.refresh()
