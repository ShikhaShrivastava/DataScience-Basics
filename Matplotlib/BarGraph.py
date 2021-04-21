#Matplotlib- "Bar Graph"

import matplotlib.pyplot as plt

x1=[10,20,30,40,50]
y1=[15,25,35,45,55]
plt.bar(x1,y1,color='red')

x2=[15,25,32,5,55]
y2=[20,49,25,35,15]
plt.bar(x2,y2,color='blue')


plt.title('bargraph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
