#encoding:utf-8
import urllib
import urllib2
import re

url = 'http://www.qiushibaike.com/hot/'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
try: 	
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile('<div class="content">.*?</div>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		print item
		print '----------------------------------------------------------------------------------------------------------'
		print '----------------------------------------------------------------------------------------------------------'
		print '----------------------------------------------------------------------------------------------------------'
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason


	