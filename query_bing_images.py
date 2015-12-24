from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import sys

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')

if len(sys.argv) != 2:
    print "Invalid args.\nUSAGE: python query_bing_images.py IMAGE_TYPE"
    sys.exit()

image_type = sys.argv[1]
query = sys.argv[1] 
url = "http://www.bing.com/images/search?q=" + query + "&qft=+filterui:color2-bw+filterui:imagesize-large&FORM=R5IR3"

soup = get_soup(url)
images = [a['src'] for a in soup.find_all("img", {"src": re.compile("mm.bing.net")})]

for img in images:
    raw_img = urllib2.urlopen(img).read()
    cntr = len([i for i in os.listdir("images") if image_type in i]) + 1
    f = open("images/" + image_type + "_" + str(cntr), 'wb')
    f.write(raw_img)
    f.close()
