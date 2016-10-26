import praw
import OAuth2Util
from time import sleep

r = praw.Reddit(user_agent = "Nintendo Switch Hype Train v1.0 by /u/aparker314159")
o = OAuth2Util.OAuth2Util(r)

subname = "aparkerbotplayground"
finished = set()
onboard = 0

def genmessage(count):
    yield "#ALL ABOARD THE SWITCH HYPE TRAIN!\n#[CHOO CHOO!](http://imgur.com/y9igYes)\n" + str(onboard) + " people onboard the hype train!\n\n^___________________________________________________________________\n\n^This ^is ^a ^bot, ^and ^this ^action ^was ^performed ^automatically.\n\n^Please ^contact ^[\/u\/aparker314159](https://reddit.com/user/aparker314159) ^for ^any ^questions ^or ^comments."

while True:
    subreddit = r.get_subreddit(subname)
    comments = subreddit.get_comments(limit=200)
    for c in comments:
        if c in finished:
            break
        if "hype train" in (c.body).lower() and c.author.name != "testbotaparker314159":
            onboard = onboard + 1
            message = next(genmessage(onboard))
            c.reply(message)
        finished.update([c])
    sleep(900)
    o.refresh()
