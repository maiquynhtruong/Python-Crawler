
import requests
import urllib2
import praw
import time
import json
import re
import sys

challengeList = {}

def startCrawling():
	nextPage = ''
	for i in range(3):
		time.sleep(10)
		print '\n\nPage ' + str(i+1) + '\n\n'
		jsonFile = requestJson(pageLink + nextPage)
		nextPage = jsonFile['after']
		jsonFile = jsonFile['children']
		for item in jsonFile:
			link = item['data']['permalink']
			title = item['data']['title']
			p = re.compile('(Easy|Intermediate|Hard)')
			m = p.search(title)
			if m:
				category = m.group() #The word that matches
				sortChallenge((title, link), category)


def sortChallenge(submisison, type):
	print submisison
	if type not in challengeList:
		# if the challenge does not exist yet, create a new one
		challengeList[type] = set()
	challengeList[type].add(submisison)

def requestJson(url):
	
	file = urllib2.urlopen(url)
	text = file.read()
	return json.loads(text)['data']


def displayChallenges():
	f = open('output.md', 'w')
	print 'Easy challenges\n\n'
	f.write('\n\nEasy challenges\n\n')
	for i in challengeList['Easy']:
		# print i[0]
		f.write('[' + str(i[0]) + '](' + str(i[1]) + ')' + '\n')
	print 'Intermediate challenges''\n\n'
	f.write('\n\nIntermediate challenges\n\n')
	for i in challengeList['Intermediate']:
		# print i
		f.write('[' + str(i[0]) + '](' + str(i[1]) + ')' + '\n')
	print 'Hard challenges\n\n'
	f.write('\n\nHard challenges\n\n')
	for i in challengeList['Hard']:
		# print i
		f.write('[' + str(i[0]) + '](' + str(i[1]) + ')' + '\n')

reload(sys)
sys.setdefaultencoding('utf-8')

subreddit = 'dailyprogrammer'
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
pageLink = 'https://www.reddit.com/r/dailyprogrammer.json?limit=100&count=100&after='

startCrawling()
displayChallenges()


