#amys_lambda/my_mod.py

#from lecture - function
def enlarge(n):
    """
    Multiplies a number by 100

    Param: a (numeric/ float /int) the number to enlarge

    Return the enlarged number(numeric)

    """
    return n * 100

#my own function - Function to split dates ("MM/DD/YYYY") into multiple columns:
# def split_date(df_in, column_name):
#     """
#     Param: df_in (pandas.DataFrame) containing a column called 'date'

#     return the year, month and day into seperate columns

#     """
#     df_in['year'] = df_in[column_name].dt.year
#     df_in['month'] = df_in[column_name].dt.month
#     df_in['day'] = df_in[column_name].dt.day
#     return df_in
    

if __name__ == "__main__":
    #only if running from command line, invoke the following code:
    #otherwise, don't 

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("Please input a number to enlarge: "))
    print(enlarge(y))

    