import requests,json

url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
proxies={'http':'117.50.36.103:443'}
header={'Cookie':'user_trace_token=20200301185113-a8e65304-7fbd-4695-8e17-f769b8715fb9; LGUID=20200301185113-3f1eab35-99c3-4f04-8ba0-03ed88ea9886; _ga=GA1.2.529237314.1583059875; _gid=GA1.2.2014400842.1583059875; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217095b974d9cf-08c5d5279e4385-39697402-2073600-17095b974da1a%22%2C%22%24device_id%22%3A%2217095b974d9cf-08c5d5279e4385-39697402-2073600-17095b974da1a%22%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1583059875,1583107156; gate_login_token=334fbbfd42fbbc3d94ae0d5bb927bcf7a50d5dec518b662a1fda9e15abe89e0a; LG_HAS_LOGIN=1; _putrc=20E137B8888E11D5123F89F2B170EADC; login=true; privacyPolicyPopup=false; LGSID=20200302152925-0669c080-3f55-4c19-9dd8-2b59c33fb2ae; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fresume%2Fperfectresume.html%3FshowQRCode%3Dtrue%26refreshTime%3D2020-03-02%2B11%253A32%26hasMyRemark%3Dtrue%26myRemarkScore%3D9%26hasabiltiyLabels%3Dtrue%26abiltiyLabels%3D%25E4%25B8%25AA%25E4%25BA%25BA%25E8%2583%25BD%25E5%258A%259B%26hasWorkExperiences%3Dtrue%26workExperienceScore%3D22%26hasLatestWorkExperience%3Dtrue%26hasProjectExperiences%3Dfalse%26projectExperienceScore%3D18%26hasEducationExperiences%3Dtrue%26eduExperienceScore%3D10%26hasSocialAccount%3Dfalse%26socialAccountScore%3D5; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fresume%2Fmyresume.html; JSESSIONID=ABAAAECABADAACHAFE9448070D35DE6C362803EDB364A8B; _gat=1; ticketGrantingTicketId=_CAS_TGT_TGT-34adaa8e60354de1924c2430dc5ddfbf-20200302152926-_CAS_TGT_; unick=%E7%94%A8%E6%88%B70836; X_HTTP_TOKEN=8b27518d64786f658354313851935a381e3523908e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1583134538; LGRID=20200302153629-b44aab0e-0a1f-4bcb-92f9-0316b892c694',
        'Host':'passport.lagou.com',
        'Referer':'https://www.lagou.com/',
        'Sec-Fetch-Dest':'script',
        'Sec-Fetch-Mode':'no-cors',
        'Sec-Fetch-Site':'same-site',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        
Data={'first':'true',
      'pn':'1',
      'kd': 'python'}

#for city in citys:
res=requests.post(url,headers=header,data=Data,proxies=proxies)
res.encoding=res.apparent_encoding
#data=res.json()
print(res.text)
#json_res=res.json()
#json_res=res.json()
#jobs=json_res['content']['positionResult']['result']
#print(jobs)
    
