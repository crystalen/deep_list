import requests,json

city=input('哪个城市')
url='http://wthrcdn.etouch.cn/weather_mini?city='+city
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
r=requests.get(url,headers=header)
r_json=r.json()
place=r_json['data']['city']
date=r_json['data']['forecast'][0]['date']
high_tem=r_json['data']['forecast'][0]['high']
low_ten=r_json['data']['forecast'][0]['low']
t=r_json['data']['forecast'][0]['type']
info=place+'\n'+date+'\n'+high_tem+'\n'+low_ten+'\n'+t
print(info)