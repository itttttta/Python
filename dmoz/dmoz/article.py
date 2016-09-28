# -*- coding:utf8 -*-
import requests

# r = requests.get('http://www.baidu.com')
# print r.encoding


import re
import chardet
import time


from lxml import etree


def test(url, timeout):
    print url

    headers = {'Host': 'blog.csdn.net',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Accept': 'text/html, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0',
               # 'Referer': 'http://blog.csdn.net/yinwenjie/article/details/52039587',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
               }

    r = requests.get(url,headers=headers)

    # r.encoding= "utf-8"

    print r.encoding
    print r.status_code
    print r.text
    # # html = html.decode('utf-8')
    # titlePattern = re.compile('<title>.*?</title>')
    # result1 = re.findall(titlePattern, html)
    #
    #
    # replaceN = re.compile('\n')
    # htmlwithoutn = re.sub(replaceN,"",html)
    # contentPattern = re.compile('<div id="content">.*?</div>')
    # contentResult = re.findall(contentPattern,htmlwithoutn)
    # print ('title')
    # for title in result1:
    #     print title
    # print ('content')
    # for item in contentResult:
    #     replaceBR = re.compile('<br />')
    #     text = re.sub(replaceBR, "\n", item)
    #     replaceNBSP = re.compile('&nbsp;')
    #     text = re.sub(replaceNBSP, "", text)
    #     print text
def multiurl():
    for index in range(35, 36):
        baseurl = "http://blog.csdn.net/yinwenjie?viewmode=contents"
        test(baseurl, 30)


if __name__ == '__main__':
    multiurl()