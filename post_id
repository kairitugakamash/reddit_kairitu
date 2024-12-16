from datetime import datetime
import json
import pandas as pd
import praw
import re
from config import user_agent, username, passwds

f = open("config_r.txt", "r")
client_id = f.readline().split(":")[1].strip()
client_secret = f.readline().split(":")[1].strip()

# create a reddit instance

reddit = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent,
                    username = username,
                    password = passwds)

filename = f"path-to_save/{post_id}.csv"

search_id = input("Enter reddit post id:\t")
submission = reddit.submission(search_id)
submission.comments.replace_more(limit=None)

comments_block = []

for comment in submission.comments.list():
    
    comments_block.append([comment.author, comment.parent_id, comment.subreddit_id, 
                           comment.depth, comment.ups, comment.downs, comment.score,
                           comment.body, datetime.fromtimestamp(submission.created_utc),                            
                           comment.created, 
                           ]) 
    comments_block_df = pd.DataFrame(comments_block, 
                                      columns=['author', 'parent_id', 'subreddit_id', 
                                               'depth', 'ups', 'downs','score', 
                                               'body', 'date_created','created'
                                               ])



comments_block_df.to_csv(filename)
