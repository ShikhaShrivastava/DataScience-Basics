#Data Frame
import pandas as pd
data1= pd.Series([1,2,3,4])
data2= pd.Series([11,12,13,14])
data3= pd.Series([21,22,23,24])

index = {'first':data1,'second':data2,'third':data3}
data=pd.DataFrame(index)
print(data)