import re
with open('成绩.txt','r')as f:
    row=f.readlines()
print(row)

result={}
for i in row:
    score=re.findall(r'\d+',i)
    sum=0
    for _ in score:
        sum=sum+int(_)
    person=re.findall(r'\D+',i)[0]
    result[str(sum)]=person
print(result)

def rank(result):
    k_list=[]
    result_r={}
    for k,v in result.items():
        k_list.append(int(k))
    k_list=sorted(k_list,reverse=True)
    i=0
    for _ in k_list:
        i+=1
        result_r[result[str(_)]]=[str(_),i]
    print(result_r)

rank(result)

