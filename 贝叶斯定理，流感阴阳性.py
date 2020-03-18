import random
n=100
test_y=n*0.01*0.9+n*0.99*0.09
true_y=n*0.01*0.9
p=true_y/test_y
t=90/(90+99*9)
print(t)
print(p,test_y,true_y)

class Man():
    flu=False
    test=False
all_people=[]
for i in range(100):
    m=Man()
    if random.random()<0.01:
        m.flu=True
    if m.flu and random.random()<0.9:
        m.test=True
    if not m.flu and random.random()<0.09:
        m.test=True
    all_people.append(m)
positive_p=[m for m in all_people if m.test]
print(len(positive_p))
positive_flu=[m for m in all_people if m.flu]
print(len(positive_flu))
print(len(positive_flu)/len(positive_p))
print(positive_flu)