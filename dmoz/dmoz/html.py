# -*- coding:utf8 -*-

import urllib
import requests
import urllib2
import re
import chardet
import time


from lxml import etree


def test(url, timeout):
    print url
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=timeout)
    html = response.read()
    html = unicode(html, "gb2312").encode("utf8")
    # html = html.decode('utf-8')
    titlePattern = re.compile('<title>.*?</title>')
    result1 = re.findall(titlePattern, html)


    replaceN = re.compile('\n')
    htmlwithoutn = re.sub(replaceN,"",html)
    contentPattern = re.compile('<div id="content">.*?</div>')
    contentResult = re.findall(contentPattern,htmlwithoutn)
    print ('title')
    for title in result1:
        print title
    print ('content')
    for item in contentResult:
        replaceBR = re.compile('<br />')
        text = re.sub(replaceBR, "\n", item)
        replaceNBSP = re.compile('&nbsp;')
        text = re.sub(replaceNBSP, "", text)
        print text
def multiurl():
    for index in range(35, 40):
        baseurl = "http://www.biqukan.com/0_184/58340"
        test(baseurl + str(index) + ".html", 30)


if __name__ == '__main__':
    multiurl()

