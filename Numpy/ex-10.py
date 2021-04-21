#addition and deletion of element in array

import numpy as np
a=np.arange(1,6)
print(a)

b=np.arange(10,60,10)
print(b)

#Addition of Element
c=np.append(b,55)
print(c)

#Adding Multiple element
d=np.append(b,[55,66])
print(d)

e= np.insert(b,2,22)
print(e)

# f=np.extend(a,[11,22]) ---->Attribute Error
