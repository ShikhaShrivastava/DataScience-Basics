import numpy as np
import sys
lst=list(range(1000000))
arr= np.arange(1000000)
print(sys.getsizeof(lst))
print(sys.getsizeof(arr))