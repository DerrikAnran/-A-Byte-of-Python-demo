#!/usr/bin/python
#Filename:spider_gakki.py
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="(http://.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,r'C:\Users\apple\Documents\pyspiders\pic\%s.jpg' %x)
        x += 1
html = getHtml("http://tieba.baidu.com/p/5079048087?red_tag=y1080182407")
getImg(html)
