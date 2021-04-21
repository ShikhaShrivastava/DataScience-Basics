#properties of Array

import numpy as np

#two dimensional array
#4 rows and 3 coloumn
np_array =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np_array)
print(np_array.ndim) #dimension
print(np_array.shape) #shape (returns no. of rows and coloumns)
print(len(np_array)) #length
print(np_array.dtype) #type of data present inside array
print(type(np_array))