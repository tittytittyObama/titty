import praw
import time
import random 

reddit = praw.Reddit(
    client_id="dd",
    client_secret="dd-QMqAdCY",
    user_agent="RedditTesting",
    username="drunkoutlaw",
    password="dd",
    check_for_async=False
)


 import random
import time
def karma():
	try:
    messages = ["BIRD","BEAK"]
    for submissions in reddit.subreddit("iasip+the_dennis").stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
  except:
    time.sleep(300)
    karma()
karma()
