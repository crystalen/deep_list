a=[x for x in range(100)]
b=[]
for i in a:
    if ('7' in str(i)) or i%7==0:
        b.append(i)
print(b)
pp=[]

for i in range(b[1]):
    pp.append(i)
for i in range(b[1],(b[1]-(b[2]-b[1])),-1):
    pp.append(i)
for i in range((b[1]-(b[2]-b[1])),(b[1]-b[2]+b[1]+b[3]-b[2])):
    pp.append(i)
print(pp)
pingpang=[0]
for x in range(1,len(b)-2):
    if x %2==0:
        for i in range((pingpang[-1]-1),(pingpang[-1]-1-(b[x]-b[x-1])),-1):
            pingpang.append(i)
    elif x%2!=0:
        for i in range((pingpang[-1]+1),(pingpang[-1]+(b[x]-b[x-1]+1))):
            pingpang.append(i)
print(pingpang)


