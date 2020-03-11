import csv,requests,json,time

def write():
    with open ('单词本.csv','a',encoding='utf-8')as f:
        w=csv.writer(f)
        while True:
            word=input('输入新单词')
            mean=meaning(word)
            date=time.strftime('%d/%m/%Y')
            print(word,'-',mean,'-',date)
            w.writerow([word,mean,date])
            c=input('退出按 q, 其他继续录入')
            if c=='q':
                return
            else:
                continue
                
def search():
    with open ('单词本.csv','r',encoding='utf-8-sig')as f:
        reader=csv.reader(f)
        while True:
            ask=input('输入查询单词')
            for row in reader:
                if ask in row[0] or ask in row[1]:
                    print(row)
            c=input('录入按 y,退出按 q，其他继续查询')
            if c=='y':
                write()
            elif c=='q':
                return
            else:
                continue       


def meaning(word):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    header={'Host':'fanyi.youdao.com',
           'Origin':'http://fanyi.youdao.com',
           'Referer':'http://fanyi.youdao.com/',
           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    data={'i':word,
          'from':'AUTO',
          'to':'AUTO',
          'smartresult':'dict',
          'client':'fanyideskweb',
          'doctype':'json',
          'version':'2.1',
          'keyfrom':'fanyi.web',
          'action':'FY_BY_REALTlME'}
    res=requests.post(url,headers=header,data=data)
    json_tran=res.json()
    translate=json_tran['translateResult'][0][0]['tgt']
    return translate

while True:
    a=input('录入：1，查询：2，退出：3')
    if a=='1':
        write()
    elif a=='2':    
        search()
    elif a=='3':
        break




