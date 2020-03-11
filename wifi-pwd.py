import itertools as its
import datetime,string

start=datetime.datetime.now()
word=string.digits
r=its.product(word,repeat=8)
with open(r'/Users/luyujin/文档/python/深度学习/deep_list/password.txt','w')as f:
    for i in r:
        f.write(''.join(i))
        f.write(''.join('\n'))
        print(i)
print('done')
end=datetime.datetime.now()
print(end-start)
