import itertools,string
menu=[690,1500,2100,1740,2140,2080]

item=itertools.combinations_with_replacement(menu,6)
count=0
#选6个东西，总价不超过10000，有多少种组合：
def q1():
    for i in item:
        if sum(i)<10000:
            count=count+1
            print(i)
    print(count)

#上面条件＋690那样东西，最多选一个，怎么组合：
def q2():
    for i in item:
        if sum(i)<=10000:
            a=0
            for x in i:        
                if x==690:
                    a=a+1
            if  a<=1:
                count+=1
                print(i)
    print(count)

#不限选择个数，总价不超过10000，有多少组合：
def q3():
    a=sorted(menu)
    num=int(10000/int(a[0]))
    for i in range(num):
        items=itertools.combinations_with_replacement(menu,i)
        for j in items:
            if sum(j)<10000:
                count+=1
                print(j)
    print(count)

