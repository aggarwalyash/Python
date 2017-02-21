import requests, os, bs4
import urllib.request
from bs4 import BeautifulSoup
start = int(input())
end = int(input())
for i in range(start,end+1):
    url = "http://xkcd.com/"
    url += str(i) + "/"
    print("Downloading page %s" % url) 
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text)
    comic = soup.select("#comic img")
    comic_url = 'http:' + comic[0].get('src')
    print("Downloading image %s" %s(comic_url))
    urllib.request.urlretrieve(comic_url)
    print("Downnloaded")
