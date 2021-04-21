#Matplotlib- "scatter plot"

import matplotlib.pyplot as plt
import numpy as np
x1=np.random.randint(10,20,10)
#print(x)
y1=np.random.randint(10,30,10)
#print(y)
plt.scatter(x1,y1,color='orange',label='set1')

x2=np.random.randint(10,15,10)
#print(x)
y2=np.random.randint(10,20,10)
#print(y)
plt.scatter(x2,y2,color='green',label='set2')
plt.title('Scatter Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
#plt.plot(x,y)
plt.show()
