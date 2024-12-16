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
  
# to view live stream

subreddit = reddit.subreddit('politics')

for comment in subreddit.stream.comments():
    try:
        print('\n\nComment: ')
        print(comment.body)
        
        
    #except praw.exceptions.PRAWException as e:
    except Exception as e:
        pass
'''
for submission in subreddit.stream.submissions():
    try:

        print('\nAuthor: ', submission.author, '\t ID', submission.id)
        #print(submission.author)
        print('\n\nSubmission: ')
        print(submission.title)
        
    #except praw.exceptions.PRAWException as e:
    except Exception as e:
        #pass
        print(str(e))
  '''

 '''
  submits_politics = []
for submission in subreddit.stream.submissions():
    try:

        print('\nAuthor: ', submission.author, '\t ID', submission.id)
        #print(submission.author)
        print('\n\nSubmission: ')
        print(submission.title)
        submits_poolitics.append(submission.author)
        submits_poolitics.append(submission.id)
        submits_poolitics.append(submission.title)
    #except praw.exceptions.PRAWException as e:
    except Exception as e:
        #pass
        print(str(e))
  '''
