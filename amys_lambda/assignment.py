
import pandas as pd

#State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)
#take a pandas DF that has a state abbrevations
#....and write a function to add corresponding state names

def add_state_name():
    pass


if __name__ == "__main__":
    pass

    df = pd.DataFrame({"abbrevations": ["CA", "CO", "CT", "TX", "DC"]})
    print(df.head())
    df2 = pd.DataFrame({"abbrevations": ["OH", "MI", "CT", "TX", "PA"]})
    print(df2.head())