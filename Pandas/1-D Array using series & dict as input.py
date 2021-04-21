#Pandas
#pandas makes use of Data Structures like Series and DataFrames in order to store data.
#Series
#creation of 1-D Array using series by taking dictionary as input

import pandas as pd
data={'firstname':'Santhosh','lastname':'Shekhar','Designation':'Tech-Trainer','Salary':35000}
pd_series=pd.Series(data)
print(pd_series)