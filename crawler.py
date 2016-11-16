import requests
import urllib2
import praw
import time
import json

challengeList = {}

def start():
	r = praw.Reddit(user_agent = user_agent)
	subReddit = r.get_subreddit('dailyprogrammer')
	subReddit.get_submissions()
	submission = 'Title'
	# if 'Challenge ' in submission.title:
		# write regex to get the challenge type
		# Three categories: hard, intermediate and easy
	category = 'hard'
	sortChallenge(submission, category)
	print requestJson(subReddit.)


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

url = 'https://www.reddit.com/r/dailyprogrammer/.json'
user_agent = 'Reddit Crawler 0.1 (by /u/mqtruong)'
user_name = 'mqtruong'
start()
