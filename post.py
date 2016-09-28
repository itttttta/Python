import urllib2
 
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://github.com/login"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()