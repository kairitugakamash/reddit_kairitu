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
# specify a subreddit example # https://www.reddit.com/r/programming/rising/ or https://www.reddit.com/r/Python/
# can sort  by Hot, New, Top, rising, gilded
#keyword = input("Enter string to search :\t")

# Collecting posts under "hot" Label

def hot_post(keyword):
    
    subreddit = reddit.subreddit(keyword)
    
    hot_posts = subreddit.hot(limit=200)
    

    hot_posts_output = []
    # get thread ids

    for submission in hot_posts:

        hot_posts_output.append([submission.title, submission.author, submission.id, 
                                 submission.num_comments, datetime.fromtimestamp(submission.created_utc), 
                                 submission.created_utc,submission.domain,
                                 submission.ups, submission.downs,submission.upvote_ratio,
                                 submission.shortlink, submission.subreddit_name_prefixed, submission.subreddit_id,
                                 submission.subreddit_type]) 



    # put it into a dataframe

        hot_posts_output_df = pd.DataFrame(hot_posts_output, 
                                      columns=['title','author','id', 'num_comments','date_created', 'created_utc','domain',
                                               'ups','downs', 'upvote_ratio', 'shortlink', 'subreddit_name_prefixed', 
                                               'subreddit_id', 'subreddit_type']).sort_values(by='num_comments', ascending=False)

    return hot_posts_output_df

# Collecting posts under "new" Label

def new_post(keyword):
    
    subreddit = reddit.subreddit(keyword)
    
    new_posts = subreddit.hot(limit=200)
    #rising_posts

    new_posts_output = []
    # get thread ids

    for submission in new_posts:

        new_posts_output.append([submission.title, submission.author, submission.id, 
                                 submission.num_comments, datetime.fromtimestamp(submission.created_utc), 
                                 submission.created_utc,submission.domain,
                                 submission.ups, submission.downs,submission.upvote_ratio,
                                 submission.shortlink, submission.subreddit_name_prefixed, submission.subreddit_id,
                                 submission.subreddit_type]) 



    # put it into a dataframe

        new_posts_output_df = pd.DataFrame(new_posts_output, 
                                      columns=['title','author','id', 'num_comments','date_created', 'created_utc','domain',
                                               'ups','downs', 'upvote_ratio', 'shortlink', 'subreddit_name_prefixed', 
                                               'subreddit_id', 'subreddit_type']).sort_values(by='num_comments', ascending=False)

    return new_posts_output_df


# Collecting posts under "top" Label

def top_post(keyword):
    subreddit = reddit.subreddit(keyword)
    
    top_posts = subreddit.rising(limit=200)
    #rising_posts

    top_posts_output = []
    # get thread ids

    for submission in top_posts:

        top_posts_output.append([submission.title, submission.author, submission.id, 
                                 submission.num_comments, datetime.fromtimestamp(submission.created_utc), 
                                 submission.created_utc,submission.domain,
                                 submission.ups, submission.downs,submission.upvote_ratio,
                                 submission.shortlink, submission.subreddit_name_prefixed, submission.subreddit_id,
                                 submission.subreddit_type]) 



    # put it into a dataframe

        top_posts_output_df = pd.DataFrame(top_posts_output, 
                                      columns=['title','author','id', 'num_comments','date_created', 'created_utc','domain',
                                               'ups','downs', 'upvote_ratio', 'shortlink', 'subreddit_name_prefixed', 
                                               'subreddit_id', 'subreddit_type']).sort_values(by='num_comments', ascending=False)

    return top_posts_output_df


# Collecting posts under "rising" Label

def rising_post(keyword):
    subreddit = reddit.subreddit(keyword)
    
    rising_posts = subreddit.rising(limit=200)
    #rising_posts

    rising_posts_output = []
    # get thread ids

    for submission in rising_posts:

        rising_posts_output.append([submission.title, submission.author, submission.id, 
                                 submission.num_comments, datetime.fromtimestamp(submission.created_utc), 
                                 submission.created_utc,submission.domain,
                                 submission.ups, submission.downs,submission.upvote_ratio,
                                 submission.shortlink, submission.subreddit_name_prefixed, submission.subreddit_id,
                                 submission.subreddit_type]) 



    # put it into a dataframe

        rising_posts_output_df = pd.DataFrame(rising_posts_output, 
                                      columns=['title','author','id', 'num_comments','date_created', 'created_utc','domain',
                                               'ups','downs', 'upvote_ratio', 'shortlink', 'subreddit_name_prefixed', 
                                               'subreddit_id', 'subreddit_type']).sort_values(by='num_comments', ascending=False)
        

    return rising_posts_output_df

path = "path_to_posts/all_posts/"
hot_posts_path = path + keyword +'_Hot_Reddit_Posts.csv'
new_posts_path = path + keyword +'_New_Reddit_Posts.csv'
top_posts_path = path + keyword +'_Top_Reddit_Posts.csv'
rising_posts_path = path + keyword +'_Rising_Reddit_Posts.csv'

# applying the function and exporting output to csv

new_post(keyword)
new_post(keyword).to_csv(new_posts_path)

#hot_post(keyword)
#hot_post(keyword).to_csv(hot_posts_path)

#top_post(keyword)
#top_post(keyword).to_csv(top_posts_path)

#rising_post(keyword)
#rising_post(keyword).to_csv(rising_posts_path)


