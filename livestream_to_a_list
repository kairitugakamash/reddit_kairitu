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

#to collect live stream
search_phrase = input("Enter search phrase e.g.politics:\t")
live_output_filename = f"path-to_save/{search_phrase}.csv"

subreddit = reddit.subreddit(search_phrase)

live_stream = []

for submission in subreddit.stream.submissions():
    try:

        live_stream.append([submission.title, submission.author, submission.id, 
                                 submission.num_comments, datetime.fromtimestamp(submission.created_utc), 
                                 submission.created_utc,submission.domain,
                                 submission.ups, submission.downs,submission.upvote_ratio,
                                 submission.shortlink, submission.subreddit_name_prefixed, submission.subreddit_id,
                                 submission.subreddit_type]) 
        #except praw.exceptions.PRAWException as e:
    except Exception as e:
        #pass
        print(str(e))
        
live_stream_df = pd.DataFrame(live_stream, 
                                      columns=['title','author','id', 'num_comments','date_created', 'created_utc','domain',
                                               'ups','downs', 'upvote_ratio', 'shortlink', 'subreddit_name_prefixed', 
                                               'subreddit_id', 'subreddit_type']).sort_values(by='num_comments', ascending=False)
live_stream_df.to_csv(live_output_filename)
