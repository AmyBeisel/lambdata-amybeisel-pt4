
#amys_lambda/my_script.py

import pandas as pd

from amys_lambda.my_mod import enlarge

print("Happy Tuesday Night.")

df = pd.DataFrame({"x": [1,2,3], "y": [4,5,6]})
print(df.head())

x = 5
print("ENLARGE", x, "TO", enlarge(x))

