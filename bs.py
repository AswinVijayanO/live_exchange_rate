from bs4 import BeautifulSoup
import sys
import urllib2  
r  = 'https://www.google.co.in/search?q=usd+to+inr'
import threading

def printit():
  threading.Timer(3, printit).start()
  req = urllib2.Request(r, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
  page= urllib2.urlopen(req)
  soup = BeautifulSoup(page,'html.parser')
  p = soup.find('div', attrs={'class':'vk_ans vk_bk curtgt'})  
  
  for child in p.children:
    if child.name == "span":
        name = child.text
 	print name
	break
  sys.stdout.write("\033[F")
  import csv  
  name= float(name)
  import pytz
  from datetime import datetime  
  with open('usdtoinr.csv', 'a') as csv_file:  
     writer = csv.writer(csv_file)
     writer.writerow([name, datetime.now(pytz.utc).strftime('%H:%M:%S')])
printit()
