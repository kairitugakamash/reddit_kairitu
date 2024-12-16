def clean_submission(submission):
    now_iso = dt.datetime.utcnow().isoformat()
    created_iso = dt.datetime.utcfromtimestamp(submission.created_utc).isoformat()
    try:
        submission_author = submission.author.name
    except:
        submission_author = "None"
        
    data = {
        
        "id": submission.id,
        "title": submission.title,
        "score": submission.score,
        "url": submission.url,
        "name": submission.name,
        "author": submission.author,
        "is_video": submission.is_video,
        "over_18": submission.over_18,
        "selftext": submission.selftext,
        "shortlink": submission.shortlink,
        "subreddit_type": submission.subreddit_type,
        "subreddit_subscribers": submission.subreddit_subscribers,
        "thumbnail": submission.thumbnail,
        "ups": submission.ups,
        "created_utc": submission.created_utc,
        "archived": submission.archived
    }
    
    for k,v in data.items():
        if v == "":
            data[k]="None"
    return data

def subreddit_type_submission(kind="hot", sub="writting"):
    data = []
    redt = reddit_instance()
    subreddit = redt.subreddit(sub)
    
    if kind =="hot":
        submissions = subreddit.hot()
    elif kind =="top":
        submissions = subreddit.top()
    elif kind =="new":
        submissions = subreddit.new()
    if kind =="random_rising":
        submissions = subreddit.rising()
    else:
        submissions = subreddit.random()
    
    for submission in submissions:
        comments = []
        article = clean_submission(submissions)
        article['subreddit'] = sub
        
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            comment = clean_comment(top_level_comment)
            comments.append(comment)
            
        article['comments'] = comments
        data.append(article)
        return data
    
    
def data_for_subreddit(sub):
    data = []
    for kind in ["hot", "new", "random_rising", "top"]:
        print("pulling posts from {}, {}".format(sub, kind))
        data.append(subreddit_type_submission(kind, sub))
    return data    
