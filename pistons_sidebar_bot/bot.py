import praw
import OAuth2Util
import urllib.request
import json

from time import sleep
from datetime import date

subreddit = "DPTest"
teams = {}
standings = []

def get_teams():
    http_response_teams = urllib.request.urlopen('http://data.nba.com/data/10s/prod/v1/2016/teams.json')
    unparsed_json_teams = http_response_teams.read().decode('utf-8')
    teams_data = json.loads(unparsed_json_teams)
    for team in teams_data['league']['standard']:
        if team['confName'] == 'East':
            team_id = team['teamId']
            name = team['city'] + ' ' + team['nickname']
            if name == "Detroit Pistons":
                name = "**Detroit Pistons**"
            teams.update({team_id: name})

def get_standings():
    http_response_standings = urllib.request.urlopen('http://data.nba.com/data/10s/prod/v1/current/standings_conference.json')
    unparsed_json_standings = http_response_standings.read().decode('utf-8')
    standings_data = json.loads(unparsed_json_standings)['league']['standard']['conference']['east']
    sorted_data = sorted(standings_data, key=lambda k: int(k['confRank'])) # Sort list by 'confRank'
    for s in sorted_data:
        team_id = int(s['teamId'])
        team_name = ''
        try:
            team_name = teams[str(team_id)]
        except:
            pass
        standings.append((team_name, s['win'], s['loss']))

def bot_action():
    get_standings()

    old_sidebar = r.get_settings(subreddit)['description']

    new_sidebar = old_sidebar.partition("#Division Standings")[0] # Read up to the beginning of standings table
    new_sidebar += "#Division Standings\n\n\n| Team (accurate as of " + date.today().strftime('%m/%-e/%y') + ")     | W  | L  |\n|:------------:|:----:|:----:|\n"

    for t in standings:
        new_sidebar += "| " + t[0] + " | " + t[1] + " | " + t[2] + " |\n"

    new_sidebar += "\n\n\n\n#November Schedule"
    new_sidebar += old_sidebar.partition("#November Schedule")[2]

    r.update_settings(r.get_subreddit(subreddit), description=new_sidebar)


if __name__ == "__main__":
    user_agent = "Detroit Pistons sidebar changer v0.1 by /u/aparker314159"
    r = praw.Reddit(user_agent)
    o = OAuth2Util.OAuth2Util(r)

    get_teams()
    while True:
        bot_action()
        print("Updated!")
        sleep(86400)
        o.refresh()
