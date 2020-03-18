import datetime
import time
import re
#黑色星期五
year=input('year')
for i in range(1,13):
    date=year+'-'+str(i)+'-13'
    week=datetime.datetime.strptime(date,'%Y-%m-%d').weekday()
    if week==4:
        print(date)
time.strftime('%d%m%Y')

#特殊的生日，数字没有重复
date=[(x,mm,z)for x in range(1900,2000) for mm in range(1,13) for z in range(1,31)]
#print(date)
for i in date:
    txt=str(i[0])+str(i[1])+str(i[2])
    if len(set(txt))==8 or (len(set(txt))==7 and '0' not in txt):
        print(i)


                
            

