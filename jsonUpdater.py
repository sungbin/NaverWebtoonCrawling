import re
import json
import datetime

def getLastEpisode(requestURL, titleId):
        p = re.compile("nclk_v2\(event,'lst.title','" +titleId +"','(\d+)'\)");
        res=requests.get(requestURL)
        html=res.text
        soup=BeautifulSoup(html,'html.parser')
        selectedTag=soup.select("a")
        for i, tag in enumerate(selectedTag):

                k = tag.get('onclick')

                if k:
                        if 'lst.title' in k:
                                m = p.match(k)
                                if m:
                                        return m.group(1)


def saveJSON():

	pattern = re.compile('.+titleId=(\d+)&weekday=(.+)')
	file_path = "./data.json"
	data = {}

	now = datetime.datetime.now()
	nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

	data['update time'] = nowDatetime
	data['webtoons'] = []


	requestURL = "https://comic.naver.com/webtoon/weekday.nhn"

	res=requests.get(requestURL)
	html=res.text
	soup=BeautifulSoup(html,'html.parser')

	selectedTag=soup.find_all('a')

	for tag in selectedTag:
        	if('title' in str(tag.get('class'))):

                	href = str(tag.get('href'))

                	m = pattern.match(href)
                	if m:
                        	title = str(tag.get('title'))
                        	titleId = m.group(1)
                        	weekday = m.group(2)
                        	lastEpisode = getLastEpisode('https://comic.naver.com'+href, titleId);

                        	# json format
                        	webtoon = {
                                	'title' : title,
                                	'id' : titleId,
                                	'weekday' : weekday,
                                	'lastEpisode' : lastEpisode,
                                	'href' : 'https://comic.naver.com'+href
                        	}
                        	data['webtoons'].append(webtoon);

	with open(file_path, 'w', encoding='UTF-8-sig') as outfile:
		json.dump(data, outfile, indent=4, ensure_ascii=False)

