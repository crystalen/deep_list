import random
pleft=100
mleft=100

def play():
    sum=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    return sum

while pleft> 0 and mleft>0:
    print('player:',str(pleft),'\n','mac',str(mleft))
    print('---------')
    p1=input('1:small,2:big')
    if p1=='1':
        p1s='选小'
    elif p1=='2':
        p1s='选大'
    else:
        p1=input('1 or 2')
    m1=str(random.randint(1,2))
    if m1=='1':
        m1s='选小'
    elif m1=='2':
        m1s='选大' 
    pt1=input('how much')
    mt1=random.randint(1,mleft)
    p2=input('number')
    if 2<int(p2)<19:
        p2s='压'+p2
        pt2=input('much')
        if pleft-int(pt1)-int(pt2)<0:
            pt2=input('not enough,again')
        pleft=pleft-int(pt1)-int(pt2)
    else:
        p2s='不压数字'
        pt2=0
        pleft=pleft-int(pt1)-int(pt2)
    print('player hold',pleft,'  ',p1s,':',pt1,p2s,':',pt2)
    m2=random.randint(1,2)
    if m2==1 and mleft-mt1>0:
        mac2=random.randint(3,18)
        m2s='压'+str(mac2)
        mt2=random.randint(1,mleft-mt1)
        mleft=mleft-mt1-mt2
    else:
        m2s='不压数字'
        mac2=''
        mt2=0
        mleft=mleft-mt1-mt2
    print('mac hold',mleft,'  ',m1s,':',mt1,m2s,':',mt2)
    print('****')
    out=play()

    if 2<int(out)<11:
        print(str(out),'small')
        print('****')
        if p1=='1':
            pg1=int(pt1)*2
            pleft=pleft+pg1
            print('player get',str(pg1))
        elif p1=='2':
           pleft=pleft
           print('player lost!')
        if m1=='1':
            mg1=int(mt1)*2
            mleft=mleft+mg1
            print('mac get',str(mg1)) 
        elif m1=='2':
           mleft=mleft
           print('mac lost!')

    elif 10<int(out)<19:
        print(str(out),'big')
        print('****')
        if p1=='2':
            pg1=int(pt1)*2
            pleft=pleft+pg1
            print('player get',str(pg1))
        elif p1=='1':
           pleft=pleft
           print('player lost!')
        if m1=='2':
            mg1=int(mt1)*2
            mleft=mleft+mg1
            print('mac get',str(mg1)) 
        elif m1=='1':
           mleft=mleft
           print('mac lost!')
    print('player have',str(pleft))
    print('mac have',str(mleft))
    if out==p2:
        pg2=int(pt2)*int(out)
        pleft=pleft+pg2
        print('player get num!!')
    elif out==str(mac2):
        mg2=int(mt2)*int(out)
        mleft=mleft+mg2
        print('mac get num!!')
    print('player hold',str(pleft),'\n','mac hold',str(mleft))
    if mleft==0 or pleft ==0:
        print(['mac lost the game','player lost the game'][pleft==0])
        break
    else:
        c=input('contine?')
        if c=='y':
            print('----next------')
            continue
        else:
            print('bye')
            break
  