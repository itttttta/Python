# -*- coding:utf8 -*-

import urllib
import requests
import urllib2
import re
import chardet
import numpy as np


from lxml import etree


def test(url, timeout):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=timeout)
    html = response.read()
    html = unicode(html, "gbk").encode("utf8")
    # print html
    # html = html.decode('utf-8')
    titlePattern = re.compile('<h1>.*?</h1>')
    result1 = re.findall(titlePattern, html)

    contentPattern = re.compile('<dd><a href=".*?</a></dd>')

    contentResult = re.findall(contentPattern,html)

    print ('title')
    for item in result1:
        print item
    print ('content')
    np.save('category.npy',contentResult)
    for item in contentResult:
        # replaceBR = re.compile('<br/>')
        # text = re.sub(replaceBR, "\n", item)
        # replaceNBSP = re.compile('&nbsp;')
        # text = re.sub(replaceNBSP, "", text)
        print item


if __name__ == '__main__':
    # test("http://www.biqukan.com/0_184/3940367.html", 30)
    test("http://www.baidu.com", 30)