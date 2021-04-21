#Data Frames

import pandas as pd
dict1 ={'firstname':'Santhosh','lastname':'Shekhar','Designation':'Python-Trainer','Salary':35000,'Company':'abc'}
dict2={'firstname':'Yuvraj','lastname':'Rijal','Designation':'Java-Trainer','Salary':45000}
dict2['Company']='abc'
i = {'first':dict1,'second':dict2}
data=  pd.DataFrame(i)
print(data)
