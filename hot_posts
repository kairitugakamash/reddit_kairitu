import pandas as pd
from datetime import datetime
import praw
import json
import re

subreddit = reddit.subreddit('news')
#subreddit

hot_news = subreddit.hot(limit = 2)

for submission in hot_news:
    if not submission.stickied:
        print("Title:{}, Author:{}, ID:{}, Comments:{}, Ups:{}, Downs:{}, Have we Visited:{},Likes:{}, URL:{}".format(submission.title,
                                                                                              submission.author, 
                                                                                              submission.id,
                                                                                              submission.num_comments,
                                                                                              submission.ups,
                                                                                              submission.downs, 
                                                                                              submission.visited,
                                                                                              submission.likes,        
                                                                                              submission.url))
        
        # Parsing comments
        submission.comments.replace_more(limit=0)

        posts1 = []
        for comment in submission.comments.list():
            print(20*'=')
            print("\nParent ID", comment.parent())
            print("\nCOMMENT ID", comment.id)        
            print(comment.body)

            posts1.append([comment.id, comment.likes,comment.score,comment.author, comment.body, comment.created_utc, comment.subreddit, comment.total_awards_received, comment.num_reports, comment.name, comment.created])
                        
            # to get replies to comments
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print("\nREPLY ID", comment.id)
                    print("\nREPLY", reply.body, "\n",)
                
        
posts1 = pd.DataFrame(posts1,columns=['id','likes','score','author', 'body', 'created_utc', 'subreddit', 'total_awards_received', 'num_reports', 'name', 'created'])
