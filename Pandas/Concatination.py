#concatination:

import pandas as pd
data = pd.DataFrame({'a':['1','2','3'],'b':['4','5','6']})
print(data)

data1 = pd.DataFrame({'a':['11','22','33'],'b':['44','55','66']})
print(data1)
print()
data2= pd.concat([data,data1])
print(data2)