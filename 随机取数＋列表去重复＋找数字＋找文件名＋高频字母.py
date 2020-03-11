import random,re,os,math
#在1-n中随机取m个数
#n=int(input('n,>=m'))
#m=int(input('1=<,m,<=n'))
#for i in range(m):
#    j=random.randint(1,n)
#    print(j)
#print(random.sample(range(1,n),m))  #random.sample，随机选取范围内的几个样本

#去掉列表中重复值
#t_all=[]
#for i in range(20):
#    t=random.randint(1,20)
#    t_all.append(t)
#print(t_all)     生成随机列表
#res=list(set(t_all))   方法一
#print(res)
#res1=[]           方法二
#for i in t_all:
#    if i not in res1:
#        res1.append(i)
#print(res1)
#
#找数字
#text='jkhfy38745jkdsbfw34t4k3h9ewhrr43'
#num=''.join(re.findall('\d+',text))    正则re第一种
#print(num)
#num1=''.join([i for i in text if i.isdigit()])  第二种 i for i in text生成list，if语句判断条件
#print(num1)

#
#查找文件夹下子文件中包含关键字的文件
#for item in os.listdir(r'/Users/luyujin/文档/python'):
#    try:
#        for work in os.listdir(r'/Users/luyujin/文档/python/'+item):
#            if work[-3:]=='.py':
#                print(work)
#    except:
#        continue
#os.walk遍历文件夹及所有子文件夹
#for filename in os.walk(r'/Users/luyujin/文档/python'):
#    for item in filename:
#        for f in item:
#            if f[-3:]=='txt':
#                print(f)
        
#x=u'但凡走到的地方，都是昨天，\
#    时间带不走的是岁月静好，别人承担，\
#    年年岁岁，花相似，\
#    岁岁年年，人不同。\
#    生活不止眼前的苟且，\
#    还有诗和远方。'
#seq=[c for c in x if c.strip()]
#print(seq)
#seq_len=len(seq)
#print(seq_len)
#line=math.ceil(seq_len/5)     #5是宽度，输出几列，横排输出，算好第几个矩阵形式输出
#for i in range(0,line):
#    for j in range(0,5):
#        if j*line+i<seq_len:
#            print(seq[j*line+i],end='|')
#    print('')

#找高频字母，提取，排序，数重
#text='tomorrow is another day,a beatuiful day!'
#t1=re.findall('[a-z]',text)
#t=sorted(t1)
#print(t)
#r_text=list(set(t))
#print(r_text)
#result=[]
#for i in r_text:
#    n=0
#    for j in t:
#        if j==i:
#            n=n+1
#    info=str(n)+''+i
#    result.append(info)
#print(sorted(result,reverse=True))
