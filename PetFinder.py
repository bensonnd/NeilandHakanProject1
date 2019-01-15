import pandas as pd
import pprint
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean

#   widen the head() function output
pd.set_option('display.expand_frame_repr', False)

#   import the data
#dataPath = '/Users/847756/PycharmProjects/PetFinder/data/train.csv'  ##create logic to check network connect and change path accordingly
#data = pd.read_csv(dataPath)

url = "https://docs.google.com/spreadsheet/ccc?key=1khQlSTP1_sJBjct3bs3ynSjQ3uo_p8v5bp0gl6O_bJQ&output=csv"
data = pd.read_csv(url, sep=',')

#   load data to data frame
df = pd.DataFrame(data)

#   summary and descriptive stats
print(df.head())
print(df.info())
print(df.describe().unstack())

#   reviewing relationships on subplots
plt.hist(subplots=True)
plt.show()

grouped_data = df.groupby(['Age'])
print(grouped_data['AdoptionSpeed'].describe())


#   get a list of all the column names from train.csv
columnNames = list(df.columns)

#need to create age groups
is_filtered1 = df['Type']==1
is_filtered2 = df['Type']==2
dffiltered1 = df[is_filtered1]
dffiltered2 = df[is_filtered2]
print(dffiltered2.quantile([.25, .50, .75, 1]))

plt.hist(dffiltered1['AdoptionSpeed'], bins=4, label='AdoptionSpeed by Type1')
plt.xlabel('AdoptionSpeed')
plt.title('Freq. of AdoptionSpeed (Type = 2)')
plt.axis([0, 4, 0, 8000])
plt.clear()
plt.show()

boxplotData = [dffiltered1['AdoptionSpeed'], dffiltered2['AdoptionSpeed']]
fig7, ax7 = plt.subplots()
ax7.set_title('AdoptionSpeed by Type')
ax7.boxplot(boxplotData)
plt.clear()
plt.show()


#   create cartesian product lists of the column names to evaluate the relationship between any two possible

def columnListCoeff(columnList,df):
    outputColumnlist = []
    for i in columnList:
        for j in columnList[(columnList.index(i) + 1):]:
            columnIndexi = columnList.index(i)
            columnIndexj = columnList.index(j)
            print(str(columnIndexi) + ',' + str(columnIndexj))
            emptyList = []
            emptyList.append(i)
            # create 1D array for column A
            col1 = df.iloc[columnIndexi].values
            emptyList.append(columnIndexj)
            col2 = df.iloc[columnIndexj].values
            #np.corrcoef()
            #outputColumnlist.append(emptyList)

    #create 1D array for column A

    return outputColumnlist

columnListCoeff(columnNames,data)



def arrayList(DataFrame):
    columnNames = list(DataFrame.columns)
    listArrays = []
    for i in columnNames:
        #print(i)
        columnIndexi = columnNames.index(i)
        #print(columnIndexi)
        listArrays.append(DataFrame.iloc[1:, columnIndexi])
        #print(DataFrame.iloc[:, columnIndexi])
    #return np.corrcoef([listArrays])



#Counting the number of times each breed shows up
df2 = pd.DataFrame({'count' : df.groupby( [ 'Breed1'] ).size()}).reset_index()
df2.sort_values(by='count', ascending=True)
print(df2)