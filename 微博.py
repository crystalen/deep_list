import requests
from bs4 import BeautifulSoup 
url='https://weibo.com/a/hot/realtime'
headers={'Cookie':'Ugrow-G0=589da022062e21d675f389ce54f2eae7; SUB=_2AkMpNBKaf8NxqwJRmP0Rzm7mbItyyQzEieKfaONBJRMxHRl-yT9kqnE8tRB6ArQ8dUdTWb_ZIXdzQo80nbiWWhe21iot; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W56CWzlGb4vCGmX6DhDS_6S; YF-V5-G0=260e732907e3bd813efaef67866e5183; WBStorage=42212210b087ca50|undefined',
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
r=requests.get(url,headers=headers)
bp=BeautifulSoup(r.text,'html.parser')
items=bp.find_all('h3',class_='list_title_b')
hot=[]
for item in items:
    title=item.text
    link=item.find('a')['href']
    info=title+' '+'https://weibo.com/a/hot/'+link
    hot.append(info)
print(hot)

with open('weibo.txt','w')as f:
    for i in hot:
        f.write(i+'\n')

