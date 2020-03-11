import random,re
#数列［1，1，2，3，。。。。］第三位起是前两位和
list=[1,1]
a=int(input('第几个'))
if a >2:
    for _ in range(a-2):
        n=list[-1]+list[-2]
        list.append(n)
print(list[a-1])

#打印等腰三角形
#t=int(input('num2'))
#for i in range(1,t+1):
#    print(' '*int(t-i),'* '*i)

#乘法表格
form=''
for i in range(1,10):
    row=''
    for j in range(1,i+1):
        a=str(j)+'*'+str(i)+'='+str(i*j)
        row=row+' '+a
    form=form+'\n'+row
print(form)  
#
#找出其中第一第二大的数
#list1=[]
#for i in range(5):
#    a=random.randint(1,200)
#    list1.append(a)
#print(list1)
#(m1,m2)=(list1[0],list1[1]) if list1[0]>list1[1] else( list1[1],list1[0])
#for _ in range(2,len(list1)):
#    if list1[_]>m1:
#        m2=m1
#        m1=list1[_]
#    elif m1>list1[_]>=m2:
#        m2=list1[_]
#print(m1,m2)

#除以3，5，7余数都是2的正整数
#for i in range(1,1001):
#    if i%3==2 and i%5==2 and i%7==2:
#        print(i)
#2000以内的回文数
#for i in range(1,2000):
#    str_x=str(i*i)
#    str_y=''
#    for _ in str_x:
#        str_y=_+str_y
#        if str_y==str_x:
#            print(str_y,i)

#w='蓝底哦文化v 很放得开更rt难空abs间会更热不过这些故事里的dgjbfskh，sdkfh，撒娇回复'
#b=re.findall('[a-z]+',w) #找到字符串中单词，没有＋找到字母
#c=re.sub('[a-z]','-',w) #剔除字符串中字母
#print(sorted(b))   #sorted排序

