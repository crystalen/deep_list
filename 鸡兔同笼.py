foot=input('多少只脚')
head=input('多少个头')
answer=[]
for i in range(int(head)): 
    if (int(head)-i)*4+i*2==int(foot):
        a='鸡:'+str(i)+'/ 兔:'+str(int(head)-i)
        answer.append(a)
if len(answer)==0:
    print('无解')
else:
    print(answer)    

    