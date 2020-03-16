import requests,bs4,re

url='http://jandan.net/top'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

r=requests.get(url,headers=headers)
bs=bs4.BeautifulSoup(r.text,'html.parser')
items=bs.find_all('li')
infos=[]
for i in items:
    try:
        author=i.find('div',class_='author')('strong')[0].text
        vote=i.find('div',class_='jandan-vote').get_text(strip=True)
    except:
        continue
    vote_n=re.findall(r'\d+',vote)
    info=[author,'赞同:'+str(vote_n[0]),'反对：'+str(vote_n[1]),'吐槽：'+str(vote_n[2])]
    infos.append(info)

with open('jiandan.txt','w',newline='', encoding='utf-8')as f:
    for i in infos:
        print(i)
        f.writelines([i[0],i[1],i[2],i[3],'\n'],)


