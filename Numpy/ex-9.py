#creating copy of Numpy array

import numpy as np
a= np.array([10,20,30,40,50])
b= np.array([60,70,80])
print(a)
print(a.copy()) # calling copy() using array object
c= np.copy(b)
print(c)