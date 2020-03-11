import requests,bs4

a=input('出发地拼音')
b=input('到达地拼音')
a_cn=input('出发地中文')
b_cn=input('到达地中文')
url='http://huochepiao.114piaowu.com/'+a+'-'+b+'.html'
header={'Host':'huochepiao.114piaowu.com',
        'Referer':'http://huochepiao.114piaowu.com/shanghai-tianjin.html',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
data={'startStationPy':a,
      'fromStation':a_cn,
      'endStationPy':b,
      'toStation':b_cn,
      'godate':'2020-03-25',
      'startDateVal':'2020-03-24'
}
res=requests.get(url,headers=header,data=data)
bs=bs4.BeautifulSoup(res.text,'html.parser')
train_list=bs.find_all('li',class_='a1')
station_list=bs.find_all('li',class_='a2')
for i in range(1,len(train_list)):
    tag_train=train_list[i].find('b')
    tag_station=station_list[i]
    print(tag_train.text,'\n',tag_station.text)