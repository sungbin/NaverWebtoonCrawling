from imagesDownloader import *
from jsonUpdater import *
from jsonParser import *

# setting
urllib_config()

# data.json
"""
saveJSON();
"""

# parse JSON, and crawling last episode
parseJSON();

# images download
"""
requestURL = get_requestURL(732224, 39, 'sun')
downloadImages(requestURL, "./test")
"""
