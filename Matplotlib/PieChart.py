#Pie-Chart

import matplotlib.pyplot as plt
labels = ['Python','Java','Testing','MySQL']
size=[450,350,200,100]
colors=['red','blue','green','orange']
explode=[0.1,0.1,0.1,0.1]
#explode=[0.3,0,0,0]
plt.pie(size,labels=labels,colors=colors,explode=explode)
plt.show()