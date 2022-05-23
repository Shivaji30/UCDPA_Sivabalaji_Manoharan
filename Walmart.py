import numpy as np 
import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#read the file 
df = pd.read_csv (r'D:/UCD/Walmart.csv')   
df.head()

#Data types of the columns
df.info()

#find null values 
df.isnull().sum()

#remove dulicates
df.drop_duplicates()

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year']  = df['Date'].dt.year
df.drop('Date',axis=1,inplace=True)
df.head()

#converting days and months from numerics to categories
#Mapping Dictionary
Months={1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
df['Month']= df['Month'].map(Months)
df.head()

#Boxplot Temperature
sns.boxplot(df['Temperature'])

#Creating Tempereature Category
def Temp (x):
    if x < 43:
        return 'Low Temp'
    elif x < 73:
        return 'Med Temp'
    else:
        return 'High Temp'
df['Temperature_Category'] = df['Temperature'].apply(Temp)

#Pie Chart - Yearly trend analysis
plt.pie(df.groupby('Year')['Weekly_Sales'].sum(),labels=df['Year'].unique(),autopct='%2.2f%%')
plt.title('Annual Sales')

#Stores performing well
df2 = df.groupby('Store')['Weekly_Sales'].sum()
df2.plot(kind='bar', figsize=(15, 15))

#Months Perfoming better ?
df3=df.groupby('Month')['Weekly_Sales'].sum()
df3.plot(kind='bar', figsize=(15, 15))

#Top 5 stores 
df_top = df2.nlargest(n=5)
df_top.plot(kind='bar', figsize=(15, 15))

#Least 5 stores
df_least = df2.nsmallest(n=5)
df_least.plot(kind='bar', figsize=(15, 15))

