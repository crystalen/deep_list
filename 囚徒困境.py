
action=['沉默','揭发']

def nice():
    w=action[0]
    return w

def rat():
    w=action[1]
    return w

jia_act_list=[]
yi_act_list=[]
y=int(input('几轮'))
jia=input('甲策略，1=一直沉默，2=持续揭发，3=先沉默一轮，对方上一轮沉默，继续沉默，对方上一轮揭发，从此轮起揭发')
yi=input('乙策略，1=一直沉默，2=持续揭发，3=先沉默一轮，对方上一轮沉默，继续沉默，对方上一轮揭发，从此轮起揭发')

if jia==yi=='1' or jia==yi=='3' or (jia=='1' and yi =='3') or (jia=='3' and yi=='1'):
    for i in range(y):
        jia_act_list.append(nice())
        yi_act_list.append(nice())
elif jia==yi=='2':
    for i in range(y):
        jia_act_list.append(rat())
        yi_act_list.append(rat())
elif jia=='1' and yi=='2':
    for i in range(y):
        jia_act_list.append(nice())
        yi_act_list.append(rat())
elif jia=='2' and yi=='1':
    for i in range(y):
        jia_act_list.append(rat())
        yi_act_list.append(nice())
elif jia=='2' and yi=='3':
    jia_act_list=['揭发']
    yi_act_list=['沉默']
    for i in range(1,y):
        jia_act_list.append(rat())
        yi_act_list.append(rat())
elif jia=='3' and yi=='2':
    jia_act_list=['沉默']
    yi_act_list=['揭发']
    jia_act_list.append(rat())
    yi_act_list.append(rat())

print(jia_act_list)
print(yi_act_list)

def check(jia_act_list,yi_act_list):
    jia_y=0
    yi_y=0
    for i in range(y):
        if jia_act_list[i]==yi_act_list[i]=='沉默':
            jia_y=jia_y+1
            yi_y=yi_y+1
        elif jia_act_list[i]==yi_act_list[i]=='揭发':
            jia_y=jia_y+2
            yi_y=yi_y+2
        elif jia_act_list[i]=='沉默' and yi_act_list[i]=='揭发':
            jia_y=jia_y+5
            yi_y=yi_y
        elif jia_act_list[i]=='揭发' and yi_act_list[i]=='沉默':
            jia_y=jia_y
            yi_y=yi_y+5
    return (jia_y,yi_y)

(x,y)=check(jia_act_list,yi_act_list)
print('甲获罪',x,'年','\n','乙获罪',y,'年')