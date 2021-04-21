#MATPLOTLB
#wap to obtain Linegraph using list

from matplotlib import pyplot as plt

#x=[10,20,30,40,50]
#y=[15,25,35,45,55]
x=[10,20,30,40,50,60]
y=[10,15,10,10,15,10]
plt.plot(x,y)
plt.title('Linegraph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()