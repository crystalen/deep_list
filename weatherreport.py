import requests,bs4

url='http://weather.sina.com.cn/shanghai'
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

r=requests.get(url,headers=header)
bs=bs4.BeautifulSoup(r.text,'html.parser')
location=bs.find('h4',class_='slider_ct_name')
date=bs.find('p',class_='slider_ct_date')
degree=bs.find('div',class_='slider_degree')
detail=bs.find('p',class_='slider_detail')
dirty=bs.find('div',class_='slider_warn_i_tt')
print(location.text)
print(date.text)
print(degree.text)
print(detail.text)
print(dirty.text)

