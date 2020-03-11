import random
print('start game')
while True:
    a_point=0
    b_point=0
    for i in range(5):
        a=input('num')
        b=str(random.randint(1,4))
        print(b)
        if a==b:
            a_point+=1
            if a_point==3:
                break
        elif a!=b:
            b_point+=1
            if b_point==3:
                break
    print(['a win','b win'][a_point<b_point])
    c=input('quit')
    if c=='y':
        break


