import json
import boto3
import praw
import pandas as pd

# Replace with your AWS credentials and Reddit API credentials
AWS_ACCESS_KEY_ID = 'access_key'
AWS_SECRET_ACCESS_KEY = 'secret_access_key'
REGION_NAME = 'region_name'

reddit = praw.Reddit(client_id='client_id_key',
                     client_secret='client_secret_key',
                     user_agent='testapp')

def get_reddit_posts():
    posts = []
    ml_subreddit = reddit.subreddit('London')
    for post in ml_subreddit.hot(limit=10):
        posts.append([post.title, post.score, post.id, post.subreddit.display_name, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    return posts.to_dict('records')


def send_data_to_kinesis(kinesis_client, stream_name, reddit_posts):
    for post in reddit_posts:
        partition_key = post['id']
        data = json.dumps(post) + '\n'
        encoded_data = data.encode('utf-8')
        kinesis_client.put_record(StreamName=stream_name, Data=encoded_data, PartitionKey=partition_key)

if __name__ == '__main__':
    kinesis_client = boto3.client('kinesis', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    stream_name = 'streaming_name'  

    reddit_posts = get_reddit_posts()
    send_data_to_kinesis(kinesis_client, stream_name, reddit_posts)
