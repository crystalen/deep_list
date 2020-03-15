import requests,bs4,csv

url='https://www.liepin.com/zhaopin/?'
headers={'Cookie':'abtest=0; fe_se=-1584240729146; __uuid=1584240729151.40; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1584240729; AGL_USER_ID=930e6a13-7b2f-417a-a460-b3bf8742cbe6; UniqueKey=c38c6846bbfc643d1a667e00ad0d9493; lt_auth=7usPaHJUz1v5tXnQgGsLt6lLjN%2BpAWWaoHsJhBwJ14W8U6bj4PnhQgiFqbQGxAMhwxhycsULNLj6N%2Bz%2BwHNJ4kMTwGmnkICxvv2k0H4JUeJjHuyflMXuqs7QQJslrXg6ykpgn2si; access_system=C; user_roles=0; need_bind_tel=false; new_user=true; c_flag=83d997a11590c03fd3aa3e83f118f2fe; gr_user_id=706c191f-5e64-475d-8fa0-c7a695816623; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id=5d64e7bf-ffa6-4e48-b02e-2b0139f7301e; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_sid_with_cs1=5d64e7bf-ffa6-4e48-b02e-2b0139f7301e; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_cs1=c38c6846bbfc643d1a667e00ad0d9493; grwng_uid=95659826-4432-46ea-b48b-26592364c775; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id_5d64e7bf-ffa6-4e48-b02e-2b0139f7301e=true; _fecdn_=1; char_captcha=DC1DFFEDC0A844056057D588C57A3AD7; user_name=%E9%99%86%E7%91%BE; user_photo=5d5513d3cd394174d09f1d6107u.png; imClientId=064cf1d58596f305d12fec4d3fe794b2; imId=064cf1d58596f305094eec2fdde4e569; imClientId_0=064cf1d58596f305d12fec4d3fe794b2; imId_0=064cf1d58596f305094eec2fdde4e569; __tlog=1584240729154.27%7C00000000%7CR000000058%7Cs_00_t00%7Cs_00_t00; JSESSIONID=8598AF564426B6B1A082E67A674FA6EB; __session_seq=9; __uv_seq=9; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1584241130; fe_im_socketSequence_0=2_2_2; bad1b2d9162fab1f80dde1897f7a2972_gr_cs1=c38c6846bbfc643d1a667e00ad0d9493',
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
params={'init':'-1',
         'headckid':'8115089308dea4ec',
         'flushckid':'1',
         'fromSearchBtn':'2',
         'dqs':'010',
         'imscid':'R000000058',
         'ckid':'8115089308dea4ec',
         'degradeFlag':'0',
         'key':'python',
         'siTag':'I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw',
         'd_sfrom':'search_fp_bar',
         'd_ckId':'4331e26815f53b804f7d6924fe0c96ea',
         'd_curPage':'0',
         'd_pageSize':'40',
         'd_headId':'4331e26815f53b804f7d6924fe0c96ea',
         'curPage':'1'}


r=requests.get(url,headers=headers,params=params)
bs=bs4.BeautifulSoup(r.text,'html.parser')
items=bs.find_all('div',class_='job-info')
links=[]
for i in items:
    link=i.find('h3')('a')[0]['href']   
    links.append(link)

infos=[]
for i in links:
    print(i)
    try:
        res=requests.get(i,headers=headers)
    except:
        res=requests.get('https://www.liepin.com'+i,headers=headers)
    bs1=bs4.BeautifulSoup(res.text,'html.parser')
    try:
        title=bs1.find('p',class_='job-main-title').get_text(strip=True)
    except:
        title=bs1.find('p',class_='job-item-title').get_text(strip=True)
    try:
        details=bs1.find('div',class_='resume').get_text(strip=True)
    except:
        details=bs1.find('div',class_='job-qualifications').get_text(strip=True)
    job=bs1.find('div',class_='content-word').get_text(strip=True)
    try:
        company=bs1.find('div',class_='info-word').get_text(strip=True)
    except:
        company=''
    info=[title,details,job,company]
    print(info)
    infos.append(info)

with open('liepin.csv','w',encoding='utf-8')as f:
    w=csv.writer(f)
    for i in infos:
        w.writerow([i[0],i[1],i[2],i[3]])
print('done')


