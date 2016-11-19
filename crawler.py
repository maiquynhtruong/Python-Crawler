import requests
import urllib2
import praw
import time
import json
import re

challengeList = {}

def start():
	# f = open('output.md', 'w')
	nextPage = ''
	for i in range(2):
		time.sleep(10)
		print '\n\nPage ' + str(i+1) + '\n\n'
		jsonFile = requestJson(pageLink + nextPage)
		nextPage = jsonFile['after']
		jsonFile = jsonFile['children']
		for item in jsonFile:
			title = item['data']['title']
			p = re.compile('(Easy|Intermediate|Hard)')
			m = p.search(title)
			if m:
				print 'Title:', title
				print 'Link:', suffix + item['data']['permalink']
				category = m.group() #The word that matches
				sortChallenge(submission, category)


def sortChallenge(challenge, type):
	if type not in challengeList:
		# if the challenge does not exist yet, create a new one
		challengeList[type] = set()
	challengeList[type].add(challenge)

def requestJson(url):
	
	file = urllib2.urlopen(url)
	text = file.read()
 
	return json.loads(text)['data']


def displayChallenges():
	print 'Easy challenges'
	for i in challengeList['Easy']:
		print i
	print 'Intermediate challenges'
	for i in challengeList['Intermediate']:
		print i
	print 'Hard challenges'
	for i in challengeList['Hard']:
		print i

subreddit = 'dailyprogrammer'
suffix = 'https://www.reddit.com'
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
user_name = 'mqtruong'
pageLink = 'https://www.reddit.com/r/dailyprogrammer.json?limit=100&count=100&after='
start()
displayChallenges()


