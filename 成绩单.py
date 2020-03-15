
with open('成绩.txt','r',encoding='utf-8')as f:
    r=f.readlines()
ch_sum=0
mat_sum=0
eng_sum=0
phy_sum=0
chem_sum=0
bio_sum=0
pol_sum=0
his_sum=0
geo_sum=0
result={}
for i in r[1:]:
    name=i[:2]
    ch=int(i[3:5])
    ch_sum=ch_sum+ch
    mat=int(i[6:8])
    mat_sum=mat_sum+mat
    eng=int(i[9:11])
    eng_sum=eng_sum+eng
    phy=int(i[12:14])
    phy_sum=phy_sum+phy
    chem=int(i[15:17])
    chem_sum=chem_sum+chem
    bio=int(i[18:20])
    bio_sum=bio_sum+bio
    pol=int(i[21:23])
    pol_sum=pol_sum+pol
    his=int(i[24:26])
    his_sum=his_sum+his
    geo=int(i[27:29])
    geo_sum=geo_sum+geo
    sum=ch+mat+eng+phy+chem+bio+pol+his+geo
    avg='%.2f'%(sum/9)
    result[name]=[ch,mat,eng,phy,chem,bio,pol,his,geo,sum,avg]

def avg(ss):
    return '%.2f'%(ss/30)

for v in result.values():
    for i in range(9):
        if v[i]<60:
            v[i]='不及格'
        else:
            v[i]=v[i]

rank=sorted(result.items(),key=lambda x:x[1][9],reverse=True)
result_r={}
for i in rank:
    result_r[i[0]]=i[1]

with open('成绩r.txt','w',newline='',encoding='utf-8')as f:
    f.writelines(['名次 ','姓名 ','语文 ','数学 ','英语 ','物理 ','化学 ','生物 ','政治 ','历史 ','地理 ','总分 ','平均分'+'\n'])
    f.writelines(['0 ','平均',avg(ch_sum),' ',avg(mat_sum),' ',avg(eng_sum),' ',avg(phy_sum),' ',avg(chem_sum),' ',avg(bio_sum),' ',avg(pol_sum),' ',avg(his_sum),' ',avg(geo_sum),'\n'])
    n=1
    for k,v in result_r.items():
        f.writelines([str(n),'   ',k,' ',str(v[0]),' ',str(v[1]),' ',str(v[2]),' ',str(v[3]),' ',str(v[4]),' ',str(v[5]),' ',str(v[6]),' ',str(v[7]),' ',str(v[8]),' ',str(v[9]),' ',str(v[10]),'\n'])
        n+=1








    



