from imagesDownloader import *


# requestURL = "https://comic.naver.com/webtoon/weekday.nhn"


# selectedTag=find_all(src=re.compile('data')


urllib_config()
requestURL = get_requestURL(732224, 39, 'sun')
downloadImages(requestURL, ".");
