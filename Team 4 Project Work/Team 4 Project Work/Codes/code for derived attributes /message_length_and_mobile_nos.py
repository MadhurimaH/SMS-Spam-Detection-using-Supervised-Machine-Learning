import re

# Function to extract all the numbers from the given string 
def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    #return array
    c=0
    d=0
    for i in range(0,len(array)):
          if len(array[i])==10 or len(array[i])==11:
                c=c+1
          else: d=d+1
    return d,c      

#Function to calculate length of message
def getlen(str):
    return len(str)

import pandas as pd
data=pd.read_csv('kaggle.csv')

data['Num_Phone']= data['Message'].apply(getNumbers)
print(data)

data['length'] = data['Message'].apply(getlen)
print(data['length'].head())

