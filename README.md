# my_lambda

## Installation
```sh
pip install -i https://test.pypi.org/simple/ my-lambdata-pt4

# in future maybe:
# pip install my-lambdata-pt4
```
## Usage

```py
from amys_lambda.my_mod import enlarge
from amys_lambda.my_mod import split_date
x = 5

print("ENLARGE", x, "TO", enlarge(x))
#new dataframe with date split ("MM/DD/YYYY") into multiple columns:
print(split_date(df1,"date"))

```