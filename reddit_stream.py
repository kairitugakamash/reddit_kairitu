import praw
import json
import re

f = open("config_r.txt", "r")
client_id = f.readline().split(":")[1].strip()
client_secret = f.readline().split(":")[1].strip()
user_agent = f.readline().split(":")[1].strip()
uname = f.readline().split(":")[1].strip()
pawd = f.readline().split(":")[1].strip()

# create a reddit instance

reddit = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent,
                    username = uname,
                    password = pawd)

subreddit = reddit.subreddit('python')

for comment in subreddit.stream.comments():
    try:
        parent_id = str(comment.parent())
        
        original = reddit.comment(parent_id)
        
        print('\nParent: ')
        print(original.body)
        
        print('\n\nReply: ')
        print(comment.body)
        
        
    #except praw.exceptions.PRAWException as e:
    except Exception as e:
        pass
