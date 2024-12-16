import praw
import json
import re
import pandas as pd

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

# specify a subreddit example # https://www.reddit.com/r/programming/rising/ or https://www.reddit.com/r/Python/
# can sort  by Hot, New, Top, rising, gilded

keyword = input("Enter string to search :\t")

subreddit = reddit.subreddit(keyword)
#subreddit

rising_python = subreddit.rising(limit = 10)
#rising_python

rising_python_posts = []
# get thread ids

for submission in rising_python:
    rising_python_posts.append([submission.author, submission.comments, 
          submission.id, submission.likes, submission.name, 
          submission.num_comments, submission.num_reports,
         submission.over_18, submission.thumbnail, submission.title,
         submission.url, submission.view_count, submission.visited,
         submission.whitelist_status])
    
    
# put it into a dataframe

rising_python_posts_df = pd.DataFrame(rising_python_posts, columns=['author','comments','id','likes', 'name', 
                                                                    'num_comments', 'num_reports', 'over_18', 'thumbnail', 
                                                                    'title', 'url', 'view_count', 'visited', 'whitelist_status'])
rising_python_posts_df

