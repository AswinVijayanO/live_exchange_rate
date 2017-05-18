from bs4 import BeautifulSoup
import sys
import urllib2  
from termcolor import colored
r  = 'https://twitter.com/'
req = urllib2.Request(r, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
page= urllib2.urlopen(req)
soup = BeautifulSoup(page,'html.parser')
p = soup.find('div', attrs={'class':'TweetWithPivotModule'})  
q= p.find('div', attrs={'class':'stream-item-header'})
re=q.find('span',attrs={'class':'FullNameGroup'})
t=p.find('div', attrs={'class':'js-tweet-text-container'})
s=t.find('p')
print colored('\033[1m' +re.text.replace('Verified account','')+'\033[0m','red')
print colored(s.text,'white')
