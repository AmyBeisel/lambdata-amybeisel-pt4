import pandas as pd 
#from amys_lambda.my_mod import split_date


#python amys_lambda/split_date.py
#my own function - Function to split dates ("MM/DD/YYYY") into multiple columns:
def split_date(df_in, column_name):
    """
    Param: df_in (pandas.DataFrame) containing a column called 'date'

    return the year, month and day into seperate columns

    """
    df_in['year'] = df_in[column_name].dt.year
    df_in['month'] = df_in[column_name].dt.month
    df_in['day'] = df_in[column_name].dt.day
    return df_in



if __name__ == "__main__":


# Create date and time with dataframe 
    df1 = pd.DataFrame() 
    df1['date'] = pd.date_range('1/1/2020', periods = 5, freq ='D')
    print(df1)

#new dataframe with date split ("MM/DD/YYYY") into multiple columns:
    print(split_date(df1,"date"))