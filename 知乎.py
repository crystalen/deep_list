import requests,json,csv

url_list=[]
info={}
for i in range(10):
    url='https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=1f1bd5cf600d4db6488a6174bed41f82&desktop=true&page_number='+str(i+2)+'&limit=6&action=down&after_id='+str(5+6*i)+'&ad_interval=-1'
    url_list.append(url)
    
    headers={'cookie':'_zap=5817f32f-3e7d-4cb7-873f-3f5a6c320ec6; _xsrf=77afe09a-e540-4f53-b0e9-0c1894680408; d_c0="AJBcwNNC8hCPTuHgBafThQLF16oMZRVpp1w=|1583915770"; _ga=GA1.2.1333269313.1583915773; _gid=GA1.2.1972637328.1583915773; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1583915773,1583920169; capsion_ticket="2|1:0|10:1583920180|14:capsion_ticket|44:NDA3OGU2ZmViMDdiNGE1YWE0Yjk4MzliNWFjYTc1OWY=|dfc05ee545c6dbc14a14cd77a45d8bd797e16d604123d245ef00e194eb09869a"; z_c0="2|1:0|10:1583920234|4:z_c0|92:Mi4xUERFWkJRQUFBQUFBa0Z6QTAwTHlFQ1lBQUFCZ0FsVk5hZ0pXWHdENWxjOXRpaE1URHhydGF0STZWU0FMUFZZRDVR|577be4ee190973a728f8272fade897fb79a75678ade26d180c81cb0a0ee470d2"; unlock_ticket="ABDCs1722AsmAAAAYAJVTXK7aF7SR9ivMam8kHcCYRXE_9W2IMipxw=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1583921435; _gat_gtag_UA_149949619_1=1; KLBRSID=57358d62405ef24305120316801fd92a|1583921435|1583920167',
             'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    
    r=requests.get(url,headers=headers)
    r_json=r.json()
    datas=r_json['data']
    for data in datas:
        tag_id=data['id']
        tag_type=data['target']['type']
        voteup_count=data['target']['voteup_count']
        action_txt=data['action_text']
        try:
            title=data['target']['question']['title']
        except:
            title=data['target']['title']
        info[tag_id]=[tag_type,title,voteup_count,action_txt]
print(info)

with open ('知乎.csv','w',encoding='utf-8')as f:
    w=csv.writer(f)
    w.writerow(['ID','类型','题目','赞同','话题'])
    for k,v in info.items():
        w.writerow([k,v[0],v[1],v[2],v[3]])

    


