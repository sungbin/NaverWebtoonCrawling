from imagesDownloader import *
import constant # Webtoon week view, size of each picture: 83
import re

pattern = re.compile('.+titleId=(\d+)&weekday=(.+)')


requestURL = "https://comic.naver.com/webtoon/weekday.nhn"

# /webtoon/list.nhn?titleId=747370&amp;weekday=sun

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

			# json format
			webtoon = {
				'title' : title,
				'id' : titleId,
				'weekday' : weekday
			}

			print(webtoon)




# images download
"""
urllib_config()
requestURL = get_requestURL(732224, 39, 'sun')
downloadImages(requestURL, "./test")
"""
