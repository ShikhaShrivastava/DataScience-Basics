#CPU Execution time

import numpy as np
import time

lst= list(range(1000000))
start_time = time.time()
lst =[i+2 for i in lst]
end_time = time.time()
print('The time taken by cpu to execute list is:', end_time-start_time)

array= np.array([range(1000000)])
start_time = time.time()
array=array+2
end_time = time.time()
print('The time taken by cpu to execute numpy array is:', end_time-start_time)

#In the above program it is clear that numpy is very fast in its performance.
#Whenever you work with large amount of data numpy array is 10 times faster than list
#Hence numpy array is used in Datascience
