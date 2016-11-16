import requests
import urllib2
import praw
import time
import json
import re

challengeList = {}

def start():
	res = urllib2.urlopen(frontPage)
	text = res.read() 
	jsonFile = json.loads(text)['data']['children']
	for item in jsonFile:
		title = item['data']['title']
		p = re.compile('(Easy|Intermediate|Hard)')
		m = p.search(title)
		if m:
			print 'Title:', title
			print 'Link:', suffix + item['data']['permalink']
			category = m.group() #The word that matches
	# sortChallenge(submission, category)


def sortChallenge(challenge, type):
	if type not in challengeList:
		# if the challenge does not exist yet, create a new one
		challengeList[type] = set()
	challengeList[type].add(challenge)

def requestJson(url, delay):
	while True:
		time.sleep(delay)
		file = urllib2.urlopen(url)
		res = file.read()
		return json.load(res)

def displayChallenges():
	for i in challengeList['easy']:
		print i
	for i in challengeList['intermediate']:
		print i
	for i in challengeList['hard']:
		print i

frontPage = 'https://www.reddit.com/r/dailyprogrammer.json'
subreddit = 'dailyprogrammer'
suffix = 'https://www.reddit.com'
url = 'https://www.reddit.com/r/' + subreddit
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
user_name = 'mqtruong'
allPost = 'http://www.reddit.com/r/'+ subreddit +'/search.json?restrict_sr=on&t=all'
start()


