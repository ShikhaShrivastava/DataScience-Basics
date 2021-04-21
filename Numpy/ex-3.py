#slicing

import numpy as np

#slicing the element
#var_name[start:stop:step]

array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array)
print(array.ndim)
print(len(array))
print(array[4])
print(array[1::2])

#two dimensional array
#4 rows and 3 coloumn

np_array =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np_array)
print(np_array.ndim) #dimension
#syntax : [rows(start:stop:step),coloumn(start:stop:step)]
print()
print(np_array[0:2])
print(np_array[0:2,:2])
