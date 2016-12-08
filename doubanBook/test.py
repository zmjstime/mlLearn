import urllib2
# import urllib
# import json
import socks
import socket


socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

# url = 'https://api.douban.com/v2/book/1220562'
# a = urllib2.urlopen(url).read()
# a = json.loads(a)
# for x in a:
# 	print a[x]


url = 'http://www.douban.com'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
