import urllib2
import requests
import praw
import json
import time
import re
import datetime
import sys

week = {}

def get_monday(post_time):
	monday = post_time - datetime.timedelta(days=post_time.weekday())
	# print monday.isoformat()
	# print monday.strftime('%y-%m-%d')
	return monday.toordinal()


def start_crawling():
	reddit = praw.Reddit(user_agent = user_agent)
	# sub_reddit = reddit.get_subreddit(subreddit_name = subreddit_name)
	# sub_reddit.get_new(limit=None)
	submissions = reddit.get_content(url=url, limit=100)
	for sub in submissions:
		# print str(sub) + '\n'
		addToList(submission=sub)		


def addToList(submission):
	time = datetime.datetime.utcfromtimestamp(submission.created_utc)
	monday = get_monday(time)
	title = submission.title.lower()
	# p = re.compile('Easy|Intermediate|Hard|Other')
	# res = p.search(title)
	# if res:
		# category = res.group() # string matched by re	
		
	week[monday] = week.get(monday, {'Easy' : set(), 'Intermediate' : set(), 'Hard' : set(), 'Other' : set()})
	# get the values of that monday, if it does not exist yet, create a new dict from monday
	if '[easy]' in title:
		week[monday]['Easy'].add(submission)
	elif '[intermediate]' in title:
		week[monday]['Intermediate'].add(submission)
	elif '[hard]' in title:
		week[monday]['Hard'].add(submission)
	else:
		week[monday]['Other'].add(submission)

row_template = '|{Easy}|{Intermediate}|{Hard}|{Other}|'
link_template = '[{text}]({url})'
empty_link = '[]()'
empty_dash = '**-**'
def show_challenges():
	f = open('output.md','w')
	f.write('Easy | Intermediate | Hard | Weekly / Bonus / Misc')
	f.write('-----|--------------|------|----------------------')
	for monday, contents in sorted(week.items()):
		easy = []
		for item in contents['Easy']:
			easy.append(link_template.format(text = item.title, url = item.url))
		if easy:
			easy_chal = '; '.join(easy)
		else: easy_chal = empty_link
		intermediate = []
		for item in contents['Intermediate']:
			intermediate.append(link_template.format(text = item.title, url = item.url))
		if intermediate:
			inter_chal = '; '.join(intermediate)
		else: inter_chal = empty_link
		hard = []
		for item in contents['Hard']:
			hard.append(link_template.format(text = item.title, url = item.url))
		if hard:
			hard_chal = '; '.join(hard)
		else: hard_chal = empty_link
		other = []
		for item in contents['Other']:
			other.append(link_template.format(text = item.title, url = item.url))
		if other:
			other_chal = '; '.join(other)
		else: other_chal = empty_link

		row = row_template.format(Easy = easy_chal, Intermediate = inter_chal, Hard = hard_chal, Other = other_chal)
		f.write(row)

reload(sys)
sys.setdefaultencoding('utf-8')
url = 'https://www.reddit.com/r/dailyprogrammer'
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
subreddit_name = 'dailyprogrammer'
start_crawling()
show_challenges()