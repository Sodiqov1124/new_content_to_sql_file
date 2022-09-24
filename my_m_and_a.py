import pandas as pd
import numpy as np
import sqlite3 as sql
import my_ds_babel



def my_m_and_a(content_database_1, content_database_2, content_database_3):
    df = pd.read_csv(content_database_1)
    df1 = pd.read_csv(content_database_2,sep = ";",header = None,names = ["Age","City","Gender","Name","Email"])
    df2 = pd.read_csv(content_database_3,sep = "\t",skiprows=1, names=["Gender","Name","Email","Age","City","Country"])
    gender = {"0": "Male", "1": "Female", "F": "Female", "M": "Male"}
    df["Gender"] = df["Gender"].replace(gender)
    df["FirstName"] = df["FirstName"].str.replace("\W", "").str.title()
    df["LastName"] = df["LastName"].str.replace("\W", "").str.title()
    del df['UserName']
    df["Email"] = df["Email"].str.lower()
    df["City"] = df["City"].str.replace("_", "-").str.title()
    df["Country"] = "USA"
    df1["Age"] = df1["Age"].str.replace("\D", "")
    df1["City"] = df1["City"].str.replace("_", "-").str.title()
    df1["Gender"] = df1["Gender"].str.title()
    df1["Gender"] = df1["Gender"].replace(gender)
    new = df1['Name'].str.split(expand = True)
    df1['FirstName'],df1['LastName'] = new[0],new[1]
    df1["FirstName"] = df1["FirstName"].str.replace("\W", "").str.title()
    df1["LastName"] = df1["LastName"].str.replace("\W", "").str.title()
    df1['Country'] = 'USA'
    del df1['Name']
    df1["Email"] = df1["Email"].str.lower()
    df2["Gender"] = df2["Gender"].str.replace("string_", "").str.replace("character_", "").str.replace("boolean_", "")
    df2["Gender"] = df2["Gender"].replace(gender)
    df2["Email"] = df2["Email"].str.replace("string_", "").str.lower()
    df2["Age"] = df2["Age"].str.replace("\D", "",regex = True)
    df2["City"] = df2["City"].str.replace("string_", "").str.replace("_", "-").str.title()
    pew = df2['Name'].str.split(expand=True)
    df2['FirstName'], df2['LastName'] = pew[0], pew[1]
    df2["FirstName"] = df2["FirstName"].str.replace("string_","").str.title()
    df2["LastName"] = df2["LastName"].str.replace("\W", "").str.title()
    df2["Country"] = "USA"
    df3 = pd.concat([df,df1,df2],ignore_index=True)
    new_names = ["Gender","FirstName","LastName","Email","Age","City","Country"]
    df3 = df3.reindex(columns = new_names)
    df3['FirstName'] = df3['FirstName'].astype("str")
    df3['LastName'] = df3['LastName'].astype("str")
    df3['Age'] = df3['Age'].astype("string")
    return df3
