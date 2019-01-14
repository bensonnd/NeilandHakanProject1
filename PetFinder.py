import pandas as pd
import pprint
from itertools import permutations
import numpy as np
import matplotlib as plt

pd.set_option('display.expand_frame_repr', False)

dataPath = '/Users/847756/PycharmProjects/PetFinder/data/train.csv'  ##create logic to check network connect and change path accordingly
data = pd.read_csv(dataPath)

df = pd.DataFrame(data)
print(df.head())

#print(df.Name.head(100))
#print(df.info())
#print(df.describe())

columnNames = list(df.columns)

def columnListCoeff(columnList,df):
    outputColumnlist = []
    for i in columnList:
        for j in columnList[(columnList.index(i) + 1):]:
            columnIndexi = columnList.index(i)
            columnIndexj = columnList.index(j)
            #####print(str(columnIndexi) + ',' + str(columnIndexj))
            #####emptyList = []
            #####emptyList.append(i)
            # create 1D array for column A
            col1 = df.iloc[columnIndexi].values
            #####emptyList.append(columnIndexj)
            col2 = df.iloc[columnIndexj].values
            np.corrcoef()
            #outputColumnlist.append(emptyList)

    #create 1D array for column A

    return outputColumnlist

columnListCoeff(columnNames,data)

pprint.pprint(columnListCoeff(columnNames))

def arrayList(DataFrame):
    columnNames = list(DataFrame.columns)
    listArrays = []
    for i in columnNames:
        #print(i)
        columnIndexi = columnNames.index(i)
        #print(columnIndexi)
        listArrays.append(DataFrame.iloc[1:, columnIndexi])
        #print(DataFrame.iloc[:, columnIndexi])
    return np.corrcoef([listArrays])

print(arrayList(df))

print(arrayList(df))