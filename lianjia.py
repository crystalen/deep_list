import requests,csv
from bs4 import BeautifulSoup
place=input('输入搜索区域范围拼音')
details=[]
for i in range(3):
    url='https://sh.lianjia.com/zufang/'+place+'/pg'+str(i)+'/'
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    r=requests.get(url,headers=headers)
    bs=BeautifulSoup(r.text,'html.parser')
    items=bs.find_all('div',class_='content__list--item--main')
    for item in items:
        title=item.find('p',class_='twoline').get_text(strip=True).split(' ')
        detail=item.find('p',class_='content__list--item--des').get_text(strip=True).split('/')
        price=item.find('span',class_='content__list--item-price').get_text(strip=True)
        detail.append(price)
        details.append(detail)
        
print(details)

with open('lianjia.csv','w',encoding='utf-8')as f:
    w=csv.writer(f)
    w.writerow(['位置','面积','朝向','格局','楼层','价钱'])
    for i in details:
        w.writerow([i[0],i[1],i[2],i[3],i[4].replace(' ',''),i[5]])
    
