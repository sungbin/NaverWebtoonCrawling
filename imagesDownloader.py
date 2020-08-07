import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os

import datetime

def urllib_config():
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	
def get_requestURL(titleId, story_number, weekday):
	return "https://comic.naver.com/webtoon/detail.nhn?titleId="+str(titleId)+"&no="+str(story_number)+"&weekday="+weekday

def downloadImages(requestURL, directory):
	if not(os.path.isdir(directory)):
		os.makedirs(os.path.join(directory))
	
	# btime = datetime.datetime.now()

	res=requests.get(requestURL)
	html=res.text 
	soup=BeautifulSoup(html,'html.parser')
	selectedTag=soup.select("img")

	for i, tag in enumerate(selectedTag):
		if tag.get('alt').startswith('comic'):
			imageURL = tag.get('src')
			imageType = imageURL[imageURL.rfind('.')+1 : len(imageURL)]
			newFileName = str(i) +"." + imageType
			urllib.request.urlretrieve(imageURL, os.path.join(directory,newFileName))

	# atime = datetime.datetime.now()
	# print('total time: ' + btime - atime)
