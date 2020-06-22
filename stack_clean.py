import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns



def clean_df(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with col2 values
    '''
    new_df = pd.DataFrame(columns=[col1,col2])
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if df[col1][idx] == df[col1][idx] and df[col2][idx] == df[col2][idx]:
                if val in df[col1][idx]:
                    x2 = df[col2][idx]
                    x1 = val
                    new_df = new_df.append(pd.DataFrame([[x1,x2]],columns=[col1,col2]))
#     new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
#     new_df.columns = [col1, col2]
#     new_df.sort_values('count', ascending=False, inplace=True)
    return new_df

##Function to group "At least once each week" and "At least once each day" together are 1

def frequency(row):
    if  row['StackOverflowFoundAnswer'] == "At least once each week" or row['StackOverflowFoundAnswer'] == "At least once each day":
        val = 1
    else:
        val = 0
    return val

def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df

