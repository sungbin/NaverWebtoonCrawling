from imagesDownloader import *
from jsonUpdater import *

import json
import time

# data.json
"""
saveJSON();
"""

with open('./data.json', 'r', encoding='UTF-8-sig') as json_file:
	json_data = json.load(json_file)

	update_time = datetime.datetime.strptime(json_data['update time'], '%Y-%m-%d %H:%M:%S')
	webtoons = json_data['webtoons']

	for webtoon in webtoons:
		urllib_config()
		requestURL = get_requestURL(webtoon['id'], 39, webtoon['weekday'])
		downloadImages(requestURL, "./test")
		break

# images download
"""
urllib_config()
requestURL = get_requestURL(732224, 39, 'sun')
downloadImages(requestURL, "./test")
"""
