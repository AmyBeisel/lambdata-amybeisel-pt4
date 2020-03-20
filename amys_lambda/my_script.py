
#amys_lambda/my_script.py

import pandas as pd
from amys_lambda.my_mod import enlarge
from amys_lambda.my_mod import split_date

print("Happy Tuesday Night.")

df = pd.DataFrame({"x": [1,2,3], "y": [4,5,6]})
print(df.head())

#test 1: from lecture. Make sure thing are working 
x = 5
print("ENLARGE", x, "TO", enlarge(x))

# # Create date and time with dataframe 
# df1 = pd.DataFrame() 
# df1['date'] = pd.date_range('1/1/2020', periods = 5, freq ='D')
# print(df1)

# #new dataframe with date split ("MM/DD/YYYY") into multiple columns:
# print(split_date(df1,"date"))
