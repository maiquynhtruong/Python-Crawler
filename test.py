# To test some functions like requestJson etc
import praw
import json
import urllib2
import pprint
def start():
	r = praw.Reddit(user_agent = user_agent)
	subReddit = r.get_subreddit('dailyprogrammer')
	f = open('output.txt', 'w')
	# f.write(subReddit)
	print r.get_popular_subreddits(url)
	# pprint r.get_popular_subreddits(url)
	print subReddit.get_hot()
	submission = r.get_submission(submission_id = "105aru")
	pprint.pprint(dir(submission))
	pprint.pprint(vars(submission))
	print submission.title
	print submission.selftext



url = 'https://www.reddit.com/r/dailyprogrammer/'
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
start()
