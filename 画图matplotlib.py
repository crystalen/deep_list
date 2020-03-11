import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50) #x轴－1到1，分50个点
y1=2*x
y2=x**2
plt.figure()#一个figure一个图
plt.plot(x,y1)
#plt.xlim((1,4))#show前面更换这一figure的坐标轴取值
#plt.ylim((2,8))
plt.xlabel('tian')
plt.ylabel('shi')

plt.figure(num=2,figsize=(4,4))  # num＝figure的名字，size表示图片大小
l1,=plt.plot(x,y2,color='red',linewidth=3.0,linestyle='--',label='tiny line')

new=np.linspace(-1,2,5)
plt.xticks(new)
plt.yticks([-2,-1,0,1,2],['serious','bad','okay','usual','good'])
y3=2*new
l2,=plt.plot(new,y3,color='green',linestyle='-.',label='strong line')
plt.legend(loc='upper left')
print('-------------')
plt.figure(num=3,figsize=(3,3))
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.imshow(a,interpolation='nearest',cmap='bone',origin='up')
plt.colorbar(shrink=0.92)
plt.xticks([])
plt.yticks([])

plt.show()
