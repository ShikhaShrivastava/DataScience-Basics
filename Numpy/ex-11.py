#deletion of an element

import numpy as np
a=np.arange(1,6)
print(a)

b=np.arange(10,60,10)
print(b)

#deletion of Element
c=np.delete(b,3)
print(c)

#d=np.pop(b,4)------->Attribute Error

#e=np.remove(b,10)------->Attribute Error