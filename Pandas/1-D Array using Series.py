#Pandas
#pandas makes use of Data Structures like Series and DataFrames in order to store data.
#Series
#creation of 1-D Array using series
import pandas as pd
import numpy as np
np_array = np.random.randint(1,10,5)
print(np_array)
pd_series = pd.Series(np_array)
print(pd_series)

np_array = np.random.randint(1,10,5)
index = ['1st','2nd','3rd','4th','5th']
print(np_array)
pd_series = pd.Series(np_array, index)
print(pd_series)