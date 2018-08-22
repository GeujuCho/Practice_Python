import tensorflow
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

t=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([9,8,7,9,8,3,2,4,3,4])

# 기본 그래프 만들기(dot=점)
plt.figure()
plt.scatter(t,y)
plt.show()

# 기본 그래프 만들기(dot=별)
plt.figure()
plt.scatter(t,y,marker='*')
plt.show()

# 기본 그래프 만들기(dot=삼각형)
colormap=t
plt.figure()
plt.scatter(t,y,s=50,c=colormap,marker='>')
plt.show()

# 컬러바 추가하기
colormap=t
plt.figure()
plt.scatter(t,y,s=50,c=colormap,marker='>')
plt.colorbar()
plt.show()

# 막대그래프
plt.figure()
plt.bar(t,y)
plt.show()

# 막대그래프-굵기/색깔
plt.figure()
plt.bar(t,y,width=1.0,color='r')
plt.show()

y1=np.array([3,2,4,3,4,9,8,7,9,8])
plt.bar(t,y,color='r',width=0.3,label='apple')
plt.bar(t+0.4,y1,color='g',width=0.3,label='banana')
plt.xlabel('data')
plt.ylabel('mount')
plt.legend()
plt.show()

plt.bar(t,y,color='r',width=0.3,label='apple')
plt.bar(t+0.4,y1,color='g',width=0.3,label='banana')
plt.xlabel('data')
plt.ylabel('mount')
plt.legend()
plt.xticks(t,('1Q','2Q','3Q','4Q','1Q','2Q','4Q','1Q','2Q'))
plt.yticks(y1,('1Q','2Q','3Q','4Q','1Q','2Q','3Q','4Q','1Q','2Q'))
plt.show()

plt.bar(t,y,color='r',width=0.3,label='apple')
plt.bar(-t,y1,color='g',width=0.3,label='banana')
plt.xlabel('data')
plt.ylabel('mount')
plt.legend()
plt.show()

plt.bar(t,y,color='r',width=0.3,label='apple')
plt.bar(t,-y1,color='g',width=0.3,label='banana')
plt.xlabel('data')
plt.ylabel('mount')
plt.legend()
plt.show()

# 원형그래프 만들기
plt.pie(y)
plt.show()

# 원형그래프 만들기-레이블 추가
label=['Blue','Green','Red','Cyan','Megenta','Yellow','Black','White','Blue','Green']
plt.figure
plt.pie(y,labels=label)
plt.show()