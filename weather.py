from bs4 import BeautifulSoup
import sys
import urllib2  
r  =  'http://www.accuweather.com/en/in/malappuram/193793/weather-forecast/193793'
req = urllib2.Request(r, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
page= urllib2.urlopen(req)
soup = BeautifulSoup(page,'html.parser')
p = soup.find('div', attrs={'class':'fc-status lfs'})  
t=p.find('p')
print t.text

