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
	# pprint r.get_popular_subreddits(url)
	# submissions = r.get_submissions(subreddit)
	res = urllib2.urlopen(allPost)
	text = res.read() 
	pprint.pprint(json.loads(text)['data']['children'])




url = 'https://www.reddit.com/r/' + subreddit
subreddit = 'AccidentalRenaissance'
allPost = 'http://www.reddit.com/r/'+ subreddit +'/search.json?restrict_sr=on&t=all'

user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
start()
