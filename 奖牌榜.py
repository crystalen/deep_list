import random,re
class Rank():
    def __init__(self,name):
        self.name=name
        global get_num
        get_num=[]
        
            
    def get(self):
        num=['num1','num2','num3']
        for _ in range(random.randint(1,4)):
            get_num.append(random.sample(num,1))
        return get_num
    
    def get_info(self,get_num):
        g=0
        s=0
        t=0
        for i in get_num: 
            if i[0]=='num1':
               g+=1
            elif i[0]=='num2':
                s+=1
            elif i[0]=='num3':
                t+=1
        info='金牌:'+str(g)+'/'+'银牌:'+str(s)+'/'+'铜牌:'+str(t)
        return info 

def rank_list(x):
    rank_ok=sorted(x, key=lambda i:int(re.findall(r'\d+',i)[0]),reverse=True)
    for i in rank_ok:
        print(i)

total=[]
country=['USA','EU','RUS','DEU','JAN','KOR']
for i in country:
    r=Rank(i)
    for _ in range(6):
        r_h=r.get()
    total.append(r.name+r.get_info(r_h))
#print(total)
rank_list(total)

