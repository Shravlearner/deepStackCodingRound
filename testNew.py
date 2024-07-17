#import libraries
import requests
from bs4 import BeautifulSoup
import re
def extractImage(link):
    response=requests.get(url)
    texts=(response.text)
    results= re.findall('<img[^>]+src="([^">]+)', texts)
    print(results)





print("Enter URL: ")
url=input()
answer=extractImage(url)