
import pandas as pd

#State abbreviation -> Full Name and visa versa. FL -> Florida, etc. 
# (Handle Washington DC and territories like Puerto Rico etc.)
#take a pandas DF that has a state abbrevations
#....and write a function to add corresponding state names

class CustomFrame(pd.DataFrame):
    """
    Param: my_df (pd.DataFrame) containing a column called "abbrevations"
    """
  
    def add_state_name(self):
        """
        Adds corresponding state names to dataframe. 
        Param: my_df (pd.DataFrame) containing a column called "abbrevations"
        """
        
        #new_df = self.df.copy()
        #type(my_df["abbrevations"]) #> <class 'pandas.core.series.Series'>
        #see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

        names_map = {
            "CA":  "Califorina",
            "CO":  "Colorado",
            "CT":  "Connecticut",
            "TX":  "Texas",
            "DC":  "Dist. of Columbia",
            "OH": "Ohio",
            "MI": "Michigan",
            'PA': 'Pennsylvania'
        }
    
        self["name"] = self["abbrevations"].map(names_map)
    


if __name__ == "__main__":
    pass
    print("------------------------")
    # df1 = pd.DataFrame({"abbrevations": ["CA", "CO", "CT", "TX", "DC"]})
    # #print(df.head())
    # # new_df = add_state_name(df1)
    # # print(new_df.head())
    # processor = DataProcessor(df1)
    # print(processor.df.head())
    # processor.add_state_name()
    # print(processor.df.head())

    custom_df = CustomFrame({"abbrevations": ["CA", "CO", "CT", "TX", "DC"]})
    print(custom_df.head())
    custom_df.add_state_name()
    print(custom_df.head())

    # print("------------------------")
    # df2 = pd.DataFrame({"abbrevations": ["OH", "MI", "CT", "TX", "PA"]})
    # print(df2.head())
    # new_df2 = add_state_name(df2)
    # print(new_df2.head())