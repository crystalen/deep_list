import random
def red(m,n):
    totle=int(m)
    p=int(n)
    result=[]
    for i in range(p):
        p=p-1
        if p>0 and totle>p:
            num=random.randint(1,totle)
        else:
            num=totle
        totle=totle-num
        result.append(num)
    return result

print(red(200,6))

