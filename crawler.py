import requests
from bs4 import BeautifulSoup
import urllib2

def spider(username):
	url = 'https://www.quora.com/profile/'+ username + '/following'
	# url = 'http://kukuruku.co/hub/nix/writing-a-file-system-in-linux-kernel'
	file = urllib2.urlopen(url)
	print file.read()
	print url
	# source_code = requests.get(url)
	# plain_text = source_code.text.encode('utf-8')
	# # print plain_text
	# soup = BeautifulSoup(plain_text, "html5lib")
	# for title in soup.find_all('a'):
	# 	print title
	# 	name = title.contents
	# 	# name_href = 'www.quora.com/profile/' + title.href
	# 	print name
	# 	# print(name_href)

		
spider('Mai-Truong-7')