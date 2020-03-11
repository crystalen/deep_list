import requests,json,csv

with open('dbTop250.csv','w',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['电影名','评分','演员','链接','图片'])
    for i in range(10):
        url=' https://api.douban.com/v2/movie/top250?start='+str(i*25)+'&apikey=0df993c66c0c636e29ecbb5344252a4a'
        header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        r=requests.get(url,headers=header)
        r_json=r.json()
        for i in r_json['subjects']:
            title=i['title']
            actors=''
            act_list=i['casts']
            for j in act_list:
                actor=j['name']
                actors=actors+actor
            rat=i['rating']['average']
            link=i['alt']
            img=i['images']['small']
            w.writerow([title,str(rat),actors,link,img])

print('done')


    

