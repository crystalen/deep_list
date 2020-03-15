import requests,re

gamer_info={}
gamer_name_list=[]

def get_num():
    url='https://python666.cn/cls/number/guess/'
    header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    return int(r.text)

def result(counts,a):
    b=sorted(counts)
    sum=0
    for i in counts:
        sum=sum+i
    avg=float(sum/a)
    text='玩家'+name+'玩了'+str(a)+'把. 最快'+str(b[0])+'次猜对! 平均'+str(avg)+'轮猜对'

    for k,v in gamer_info.items():
        if str(k)==name:
            n_a=int(a)+int(v[0][2:-1])
            n_avg=float((float(avg)*int(a)+float(v[2][2:-1])*int(v[0][2:-1]))/int(n_a))
            if int(b[0])<int(v[1][2:-1]):
                n_min=int(b[0])
            else:
                n_min=int(v[1][2:-1])
            text='玩家'+name+'玩了'+str(n_a)+'把. 最快'+str(n_min)+'次猜对! 平均'+str(n_avg)+'轮猜对'
        elif str(k)!=name:
            text=text
    return text

with open ('game_one_user.txt','r')as f:
    items=f.readlines()
    for i in items:
        gamer_name=re.findall(r'.*家(.*)玩',i)[0]
        gamer_count=re.findall(r'.*了(.*)把',i)[0]
        gamer_min=re.findall(r'.*快(.*)次',i)[0]
        gamer_name_list.append(gamer_name)
        gamer_avg=re.findall(r'.*均(.*)轮',i)[0]
        gamer_info[gamer_name]=['玩过'+gamer_count+'把','最快'+gamer_min+'次','平均'+gamer_avg+'轮']

name=input('叫什么啊')
if name in gamer_name_list:
    for k,v in gamer_info.items():
        if str(k)==name:
            print('历史成绩：',gamer_info[name])
else:
    print('欢迎新玩家')
a=0
counts=[]
while True:
    num=int(input('猜数字，输入1~100数字'))
    cp=get_num()
    count=1
    while num!=cp:
        if num>cp:
            print('猜大了')
        else:
            print('猜小了')
        count+=1
        num=int(input('再猜'))
    print('猜对了！猜了',count,'次')
    a+=1
    counts.append(count)
    text=result(counts,a)
    print(text)
    c=input('退出按q，其余键继续')
    print('----------------')
    if c=='q':
        break

with open ('game_one_user.txt','w')as f:
    f.write(text+'\n')

