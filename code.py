import os,re

f_contents=[]
for root, dirs, files, in os.walk(r'/Users/luyujin/文档/python/深度学习/deep_list'):
    for f in files:
        #print(f)
        f_root=os.path.join(root,f)
        try:
            open_file=open(f_root,'r',encoding='utf-8')
            f_content=open_file.readlines()
            f_contents.append(f_content)
            open_file.close()
        except:
            continue
l=0
z=0
k=0
for i in f_contents:
    for j in i:
        first_char=re.search(r'(?<=\s)*\S',j)
        if not first_char:
            k+=1
        elif first_char.group()=='#':
            z+=1
        else:
            l+=1

print('有效',l,'\n','注释',z,'\n','空白',k,'\n','总共',l+z+k)

