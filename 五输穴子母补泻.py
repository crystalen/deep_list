import time,random

wwx={'gan':['大敦','行间','太冲','中封','曲泉'],
     'dan':['足窍阴','侠溪','足临泣','阳辅','阳陵泉'],
     'xin':['少冲','少府','神门','灵道','少海'],
     'xiaoch':['少泽','前谷','后溪','阳谷','小海'],
     'pi':['隐白','大都','太白','商丘','阴陵泉'],
     'wei':['历兑','内庭','陷谷','解溪','足三里'],
     'fei':['少商','鱼际','太渊','经渠','尺泽'],
     'dach':['商阳','二间','三间','阳溪','曲池'],
     'shen':['涌泉','然谷','太溪','复溜','阴谷'],
     'pg':['至阴','通谷','束骨','昆仑','委中'],
     'sanjiao':['关冲','液门','中渚','支沟','天井'],
     'xinbao':['中冲','劳宫','大陵','间使','曲泽']}
zang={'木':'gan','火':'xin','土':'pi','金':'fei','水':'shen'}
fu={'木':'dan','火':'xiaoch','土':'wei','金':'dach','水':'pg'}
yinj={'木':'1','火':'2','土':'3','金':'4','水':'5'}
yangj={'金':'1','水':'2','木':'3','火':'4','土':'5'}
w=['木','火','土','金','水','木']
shuru=['肝、胆', '心、小肠', '脾、胃','肺、大肠','肾、膀胱','心包、三焦']

def xie(x):
    for i in range(5):
        if w[i]==x:
            zi=w[i+1]
    return zi

def bu(x):
    for i in range(1,6):
        if w[i]==x:
            mu=w[i-1]
    return mu

def bu_pan():
    #b=input('1=肝、胆  2=心、小肠  3=脾、胃  4=肺、大肠  5=肾、膀胱  6=心包、三焦')
    print('1=肝、胆  2=心、小肠  3=脾、胃  4=肺、大肠  5=肾、膀胱  6=心包、三焦')
    b=str(random.randint(1,6))
    #c=input('阴经1  or  阳经2')
    print('阴经1  or  阳经2')
    c=str(random.randint(1,2))
    print('补',shuru[int(b)-1],'其中的',['阴经','阳经'][c=='2'])
    time.sleep(2)
    if b=='1':
        mu=bu('木')
        print('本经',[wwx['gan'][int(yinj[mu])-1],wwx['dan'][int(yangj[mu])-1]][c=='2'])        
        print('母经',wwx[zang[mu]][int(yinj[mu])-1],wwx[fu[mu]][int(yangj[mu])-1])
    elif b=='2':
        mu=bu('火')
        print('本经',[wwx['xin'][int(yinj[mu])-1],wwx['xiaoch'][int(yangj[mu])-1]][c=='2'])        
        print('母经',wwx[zang[mu]][int(yinj[mu])-1],wwx[fu[mu]][int(yangj[mu])-1])
    elif b=='3':
        mu=bu('土')
        print('本经',[wwx['pi'][int(yinj[mu])-1],wwx['wei'][int(yangj[mu])-1]][c=='2'])        
        print('母经',wwx[zang[mu]][int(yinj[mu])-1],wwx[fu[mu]][int(yangj[mu])-1])
    elif b=='4':
        mu=bu('金')
        print('本经',[wwx['fei'][int(yinj[mu])-1],wwx['dach'][int(yangj[mu])-1]][c=='2'])        
        print('母经',wwx[zang[mu]][int(yinj[mu])-1],wwx[fu[mu]][int(yangj[mu])-1])
    elif b=='5':
        mu=bu('水')
        print('本经',[wwx['shen'][int(yinj[mu])-1],wwx['pg'][int(yangj[mu])-1]][c=='2'])        
        print('母经',wwx[zang[mu]][int(yinj[mu])-1],wwx[fu[mu]][int(yangj[mu])-1])
    elif b=='6':
        mu=bu('火')
        print('本经',[wwx['xinbao'][int(yinj[mu])-1],wwx['sanjiao'][int(yangj[mu])-1]][c=='2'])
    return


def xie_pan():
    #b=input('1=肝、胆  2=心、小肠  3=脾、胃  4=肺、大肠  5=肾、膀胱  6=心包、三焦')
    print('1=肝、胆  2=心、小肠  3=脾、胃  4=肺、大肠  5=肾、膀胱  6=心包、三焦')
    b=str(random.randint(1,6))
    #c=input('阴经1  or  阳经2')
    print('阴经1  or  阳经2')
    c=str(random.randint(1,2))
    print('泻',shuru[int(b)-1],'其中的',['阴经','阳经'][c=='2'])
    time.sleep(2)
    if b=='1':
        zi=xie('木')
        print('本经',[wwx['gan'][int(yinj[zi])-1],wwx['dan'][int(yangj[zi])-1]][c=='2'])        
        print('子经',wwx[zang[zi]][int(yinj[zi])-1],wwx[fu[zi]][int(yangj[zi])-1])
    elif b=='2':
        zi=xie('火')
        print('本经',[wwx['xin'][int(yinj[zi])-1],wwx['xiaoch'][int(yangj[zi])-1]][c=='2'])        
        print('子经',wwx[zang[zi]][int(yinj[zi])-1],wwx[fu[zi]][int(yangj[zi])-1])
    elif b=='3':
        zi=xie('土')
        print('本经',[wwx['pi'][int(yinj[zi])-1],wwx['wei'][int(yangj[zi])-1]][c=='2'])        
        print('子经',wwx[zang[zi]][int(yinj[zi])-1],wwx[fu[zi]][int(yangj[zi])-1])
    elif b=='4':
        zi=xie('金')
        print('本经',[wwx['fei'][int(yinj[zi])-1],wwx['dach'][int(yangj[zi])-1]][c=='2'])        
        print('子经',wwx[zang[zi]][int(yinj[zi])-1],wwx[fu[zi]][int(yangj[zi])-1])
    elif b=='5':
        zi=xie('水')
        print('本经',[wwx['shen'][int(yinj[zi])-1],wwx['pg'][int(yangj[zi])-1]][c=='2'])        
        print('子经',wwx[zang[zi]][int(yinj[zi])-1],wwx[fu[zi]][int(yangj[zi])-1])
    elif b=='6':
        zi=xie('火')
        print('本经',[wwx['xinbao'][int(yinj[zi])-1],wwx['sanjiao'][int(yangj[zi])-1]][c=='y'])
    return

while True:
    #a=input('补1 or 泻2, 其他键退出')
    print('补1 or 泻2')
    time.sleep(1)
    a=str(random.randint(1,2))
    if a=='1':
        bu_pan()
        print('--------')
        time.sleep(1)
    elif a=='2':
        xie_pan()
        print('--------')
        time.sleep(1)
    else: 
        break






