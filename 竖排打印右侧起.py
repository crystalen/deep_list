import math
x=u'但凡走到的地方，都是昨天，\
    时间带不走的是岁月静好，别人承担，\
    年年岁岁，花相似，\
    岁岁年年，人不同。\
    生活不止眼前的苟且，\
    还有诗和远方。'

seq=[c for c in x if c.strip()]
#print(seq)
seq_len=len(seq)
#print(seq_len)
width=6
line=math.ceil(seq_len/width)     
print(line)
for i in range(0,line):
    for j in range((width-1),-1,-1):
        if j*line+i<seq_len:
            a=seq[j*line+i]
        else:
            a='  '    
        print(a,end='|') 
    print('')
