from imagesDownloader import *
import json
import datetime

def parseByFavorite(favoriteLst, webtoons):
	
	for webtoon in webtoons:
			
		if not webtoon['title'] in favoriteLst: # TODO: 
			continue

		for i in range(int(webtoon['lastEpisode'])-2,int(webtoon['lastEpisode'])+1):
                	requestURL = get_requestURL(webtoon['id'], i, webtoon['weekday']) # TODO: add loop on last episode
                	downloadImages(requestURL, "./webtoons/"+webtoon['title']+"/"+str(i)+"/") # TODO: directory

def parseJSON():
		with open('./data.json', 'r', encoding='UTF-8-sig') as json_file:
			json_data = json.load(json_file)
			update_time = datetime.datetime.strptime(json_data['update time'], '%Y-%m-%d %H:%M:%S')
			webtoons = json_data['webtoons']

		r = datetime.datetime.today().weekday()
		t = ['mon','tue','wed','thu','fri','sat','sun']
		cweekday = t[r]

		for webtoon in webtoons:
			if not webtoon['weekday'] == cweekday: # TODO: 
				continue
			
			for i in range(int(webtoon['lastEpisode'])-2,int(webtoon['lastEpisode'])+1):
				requestURL = get_requestURL(webtoon['id'], i, webtoon['weekday'])
				downloadImages(requestURL, "./webtoons/"+cweekday+'/'+webtoon['title']+"/"+str(i)+"/")

		"""
		favoriteLst = ['열불 로맨스']
		parseByFavorite(favoriteLst, webtoons)
		"""
