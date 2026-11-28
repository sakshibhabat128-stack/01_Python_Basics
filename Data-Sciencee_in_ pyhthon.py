# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 17:00:08 2026

@author: YADNYESH
"""
#data structure in python
import pandas as pd
pd.__version__#my version is 2.3.3
##################
#aSeries is used to model one dimensitonal array
#Defiend Series
import pandas as pd
songs2 = pd.Series([145,142,38,13],name='counts')
#it is easy to inspect the index of a series (or data frame)
songs2.index
#this index can be string based as well,
#in which case pandas indicates
#that the datatype for the index is object (not string)
songs3 = pd.Series([145,142,38,13],name='counts',index =['Paul','John','George',"Ringo"])
songs3.index
songs3
################# 
#the NaN value
#this value stands for not A number,
#and is usually ignored in arithmatic
#operations(similar to NULL in SQL).
#if you load data from a csv file,
#An empty value for an otherwise
#numeric collumn will become Nan.
#numeric column will become NAN.
import pandas as pd
f1=pd.read_csv('age.csv')

f1=pd.read_csv('c:/3-Ds_python/age.csv')
f1

df=pd.read_excel('c:/3-Ds_python/Bahaman.xlsx')
##################
#None,NAN,nan and null are synonyms
#the series object behaves similarly to
#a Numpy array.
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
#142
numpy_ser[1]
#They both have methods in comman
songs3.mean()
numpy_ser.mean()
#################
#THE PANDAS SERIES DATA STRUCTURE PROVIDES
#Support FOR THE BASIC CRUD
#Operations-create,read,update, and delete.
#Creation
import pandas as pd
george= pd.Series([10,7,1,22],
index =['1968','1969','1970',],
name='George_Songs')
george
######################
13-02-26
#Reading
#to read or select the data from a series
george['1968']

george['1970']
#we can iterate over data in a series
#as well.when iterating over a series

for item in george:
    print(item)
###################
#updating
george['1969'] = 68
george['1969']
george

s =pd.Series([2,3,4],index =[1,2,3] )
del s[1]
s
#incomplete
##########3
#convert types
import pandas as pd
songs_66 = pd.Series([3,None,11,9],
index =['George','Ringo','John','Paul'],
name='counts' )
songs_66
songs_66.dtypes
###########3
#dtype('float64')
songs_66 = pd.Series([3,None,11,9],
     index=['George','Ringo','John','Paul'],
     name = 'counts',
     dtype ='int64'
)

print(songs_66)
print(songs_66.dtypes)


pd.to_numeric(songs_66.apply(str))
#Only numeric values can be converted,there is none
#error
#specialized function just for numeric conversion(to int64 or float 64)
#can try to convert non-numeric string where possible
#Has will be error
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass errors ='coerce'
#we can see that it supports many formats
songs_66.dtypes
#Dealing with None
#the fillna method will replace them with a given value,=1
songs_66 =pd.Series([3,None,11,9],
index=['George','Ringo','John','Paul'],
name='counts')
print(songs_66.dtypes)
songs_66=songs_66.fillna(-1)
songs_66
songs_66=pd.to_numeric(songs_66.apply(str))
print(songs_66.dtypes)

songs_66 =songs_66.fillna(-1)
songs_66=songs_66.apply(str)
print(songs_66.dtypes)
#OR
songs_66 = songs_66.fillna(-1).astype(str)
songs_66.dtypes #object -meaning string values
print(songs_66.dtypes) 

#dropna method
songs_66 =pd.Series([3,None,11,9],
index=['George','Ringo','John','Paul'],
name='counts')
songs_66=songs_66.dropna()
songs_66
##########
#Append,combining and joining two series
songs_69 =pd.Series([7,16,21,39],
index=['Ram','Sham','Ghansham','Shivam'],
name='counts')
#to concatenate two series together,simply use the append method
songs=pd.concat([songs_66,songs_69])
songs
################
#plotting Series
import matplotlib.pyplot as plt
fig =plt.figure()
songs_69.plot()
plt.legend()
####################
fig =plt.figure()
songs_69.plot(kind='bar')
songs_69.plot(kind='bar' ,color='r')
plt.legend()
#####################
#learning how to plot series in histogram
import numpy as np
data = pd.Series(np.random.randn(500),name='500_random')
fig = plt.figure()
ax =  fig.add_subplot(111)
data.hist()
####################
16-02-26
#Create using constructor
#Create pandas DataFrame From List
import pandas as pd
technologies =[["Sparks",20000,"30days"],
               ["pandas",20000,"40days"]
               ]

df=pd.DataFrame(technologies)
print(df)
#since we have not given labels to columns and
#indexes,DataFrame by default assigns
#incremental sequence numbers as labels
#to both rows and column,these are called index

#add column And label
column_names=["courses","fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
##############
df.types
######################
#you can also assign custom
#data types to columns.
#set custom type to DataFrame
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas",
               "Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration ':['30day','40days','35days', '40days','60days',
                 '50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)
#convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
#change all column to same type
df =df.astype(str)
print(df.dtpyes)
#change type for one or multiple columns
df = df.astype({"fee":int,"Discount":float})
print(df.dtypes)#Error
#convert Data type for all columns in a list
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee','Discount']
df[cols] = df[cols].astype('float')
df.dtypes
#Ignores error
df = df.astype({"Courses":int},errors='ignore')
df.dtypes
#generate Error
df = df.astype({"Courses":int},errors='raise')
#converts feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount']) 
df.dtypes

##############################
import pandas as pd
#Create DataFrame from Dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }

df = pd.DataFrame(technologies)
df
####################
#convert DataFrame to csv
df.to_csv('data_file.csv')
##############
#Create DataFrame From CSV File

df = pd.read_csv('data_file.csv')
########################
#pandas DataFrame- Base Operations
#create DataFrame with None/Null to work with example
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df =pd.DataFrame(technologies,index=row_labels)
print(df)
#############################3
#DataFrame Properties(dont have parenthesis)
df.shape 
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info#(usually used as function not properties)
####################3
#Accessing one column contents
df['Fee']
#Accessing two columns contents
cols=['Fee','Duration']
df[cols]
df[['Fee','Duration']]
#Select certain rows and assign it to another dataframe
df2=df[6:]
df2=df[:6]
df2
##############3
#Asseccinig certain cell from column 'Duration'
df['Duration'][3]
#Substracting specific value from a column
df['Fee'] = df['Fee'] - 500
df['Fee']
#PANDAS to manipulate dataFrame
#Describe Dataframe
#Describe Data Frame for all numeric columns
df.describe()
#it will show 5 number summary
######################
#rename ()- Renames pandas Dataframe columns
df = pd.DataFrame(technologies,index=row_labels)
columns =['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'},axis=1)
df2 = df.rename({'C':'c3','D':'c4'},axis='columns')
df2 = df.rename(columns={'A':'c1','B':'c2'})
##########################
#Drop DataFrame Rows and Columns
df =pd.DataFrame(technologies,index=row_labels)

#Drop rows by labels
df1 =df.drop(['r1','r2'])
df1
#Delete Rows by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#Delete rows by index range
df1=df.drop(df.index[2:])
df1
#when you have default indexes for rows
df = pd.DataFrame(technologies) 
df1 =df.drop(0)
df1
df = pd.DataFrame(technologies)
df1 =df.drop([0,3],axis=0)#it will delete row0 to row3
df1
df1 = df.drop(range(0,2))#it will delete 0 and 1 
df1
######################
#Dropping of columns
#######################
17-02-26
import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })

df = pd.DataFrame(technologies)
print(df)
#Drop columns by names
#Drop 'Fee' column
df2=df.drop(["Fee"],axis=1)
print(df2)

#Explicitly using parameter name 'labels'
df2=df.drop(labels=["Fee"],axis=1)

#Alternatively you can also use columns instead of labels.
df2=df.drop(columns=["Fee"],axis=1)
########################
#Drop column by index
print(df.drop(df.columns[1],axis = 1))

df = pd.DataFrame(technologies)
#using inplace=True(use when drive from original DataFrame)
df.drop(df.columns[2],axis=1,inplace=True)
print(df)
###################
df = pd.DataFrame(technologies)
#Drop two or more columns by Label Name
df2=df.drop(["Courses","Fee"],axis =1)
print(df2)
#####################
#drop two or more columns from  index
df =pd.DataFrame(technologies)

df2=df.drop(df.columns[0,1],axis=1)
print(df2)
##############################
#remove columns from DataFrame inplace
df = pd.DataFrame(technologies)

df.drop(df.columns[1],axis=1,inplace=True)
df
#using inplace True
#############################
################################3
##PANDAS select row by(positional/label) use of iloc
import pandas as pd
import  numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",
               None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days',
                '35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=row_labels)
print(df)
#df.iloc[startrow:endrow,startcolumn:endcolumn]

#Below are quick example for columns
df2=df.iloc[:,0:2]
df2
#This line uses the slicing operator to get DataFrame
#Items by index
#the first slice[:]indicates to return all rows
#the second slice specifies that only columns
#between 0 to2 (2)sholud return
df2=df.iloc[0:2,:]
df2

#slicing specific rows and columns
df3=df.iloc[1:2,1:3]
df3
#Another Example
df3=df.iloc[:,1:3]
df3

#select row by index
df2 = df.iloc[[2]]
df2= df.iloc[2]
df2


df2 = df.iloc[[2,3,6]]#select rows by index list
df2 = df.iloc[1:5]#select rows by integer index range
df2 = df.iloc[:1]#select first row
df2 = df.iloc[:3]#select first 3 rows
df2 = df.iloc[-1:]#select last row
df2 = df.iloc[-3:]#select last 3 rows
df2 = df.iloc[::2]#select alternate rows

#select Rows by index Labels
df2 =df.loc['r2']
df2 = df.loc[['r2']]  #select Row by Label
df2
df2 = df.loc[['r2','r3','r6']]  #select Rows by index label
df2 = df.loc['r1':'r5']
#This will not work like 1:5, it is using labels     #select Rows
df2

df2 =df.loc['r1':'r5':2] #select Alternate rows with in index
############################
#select multiple columns
df2 = df.loc[:,["Courses","Fee","Duration"]]
#select Random columns
df2 = df.loc[:,["Courses","Fee","Duration"]]
#select columns between two columns
df2 = df.loc[:,'Fee':'Duration']
#select columns by range
df2 = df.loc[:,'Duration']
#select columns by range
#All the columns upto Duration
df2 = df.loc[:,'Duration']
##select every alternate column
df2 = df.loc[:,::2]
####################
#########################
#pandas.DataFrame.query()by example
#Query all rows with courses equals 'Spark'
df2=df.query("Courses=='Spark'")
print(df2)
########################3
#not equals condition
df2=df.query("Courses !='Spark'")
df2
#################
######################

#pandas add column to dataframe
import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[0.1,0.2,0,0.5,0.1]
          }

df=pd.DataFrame(technologies)
print(df)
###########################
#pandas add column to DataFrame
#Add new column to the Dataframe
tutors =['Ram','Sham','Ghansham','Ganesh','Ramesh']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)
#######################
#add multiple columns to the DataFrame,
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 =df.assign(MNC=MNCCompanies,tutors=tutors)
df2
#################
#drive new column from existing column
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_percent=lambda x: x.Fee* x.Discount/100)
print(df2)
#####################
#Append column to existing pandas DataFrame
#Add new column to the existing DataFrame
df = pd.DataFrame(technologies)
df["MNCCompanies"]= MNCCompanies
print(df)
##########################
#Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'tutors',tutors)
print(df)
####################
#pandas rename column with Example
import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle",
             "Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', 
              '50days', '55days']
              })
#Rename multiple columns
df.rename(columns = {"Courses":'Courses_list','Fee':'Courses_Fee',
                    'Duration':'Courses_Duration'},inplace=True)
print(df.columns)
df.columns
########################
#Quick Example of get the number of rows in DataFrame
rows_count = len(df.index)
rows_count 
rows_count = len(df.axes[0])
rows_count
rows_count = len(df.axes[1])
rows_count
##########################3
18-02-26
#PANDAS Apply #incomplete comment 
#below are quick Examples
#using DataFrame.apply() function and column
import pandas as pd
import numpy as np

data={'A':[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]
      }

df = pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3 
df2 = df.apply(add_3)
df2
df2 =((df.A).apply(add_3))
#########################
#using apply function single column
import pandas as pd
import numpy as np
data ={'A':[1,2,3],
       'B':[4,5,6],
       'C':[7,8,9]
       }
df = pd.DataFrame(data)
 
def add_4(x):
    return x+4 
df['B'] = df['B'].apply(add_4)
df['B']
df  = pd.DataFrame(data)
#apply to multiple column
df[['A','B']] = df[['A','B']].apply(add_4)
df
#apply a lambda function to each column
df2 = df.apply(lambda x :x+4)
df2
#####################
#apply() function on selected list of multiple column
#df = pd.DataFrame(data)on add _3 code
####################
#apply lambda function to single column
#using DataFrame .apply()and lambda function
df = pd.DataFrame(data)
df['A'] =df['A'].apply(lambda x: x-2)
print(df)
###########################
#using pandas.DataFrame.map.transform()to apply function column
#using DataFrame .transform
df = pd.DataFrame(data)
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)
######################
#using pandas.DataFrame.map()to single column
df = pd.DataFrame(data)
df['A']=df['A'].map(lambda A:A/2.)
print(df)
##########################
#using Numpy function on single column
#using DataFrame.apply() & [] operator
import numpy as np
df =pd.DataFrame(data)
df

df['A'] =df['A'].apply(np.square)
print(df)
##############################3
#using numpy.square()method
#using numpy.square() and [] operator
df = pd.DataFrame(data)
df
df['A'] = np.square(df['A'])
print(df)
#######################
#pandas groupby () with Example
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })

df=pd.DataFrame(technologies)
print(df)
#use groupby() to compute the sum
df2 = df.groupby(["Courses"]).sum()
print(df2)
####################
#group by multiple columns
df = pd.DataFrame(technologies)
df2 = df.groupby(['Courses','Duration']).sum()
print(df2)
#######################
#Add index to the grouped data
#Add Row Index to the group by result
df3= df.groupby(['Courses','Duration']).sum().reset_index()
print(df3)
########################33
#pandas get columns name from DataFrame
import pandas as pd
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df =pd.DataFrame(technologies)
print(df)
df.columns
#get the list of all column names from DataFrame
column_headers =list(df.columns.values)
print("The column Header :", column_headers)
####################33
#using list(df) to get the column header as a list
column_headers = list(df.columns)
column_headers
#using list (df) to get the list of all column names
column_headers =list(df.columns)
column_headers
#####################
#pandas shuffle DataFrame Rows
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df = pd.DataFrame(technologies)
print(df)
#pandas shuffle DataFrame Rows
#Shuffle the DataFrame rows & return all rows
df1 = df.sample(frac = 1)
print(df1)
df1 = df.sample(frac = 0.5)
print(df1)
###################### 
# reset shuffle index
df1 = df.sample(frac = 1).reset_index()
print(df1)
######################3
#drop shuffle index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)
#####################333
#joins
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
################################
df3=df1.join(df2,lsuffix="left",rsuffix="right",how='inner')
print(df3)
##############################
#pandas join,by default it will join the table left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
########################
#left join &right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)
##########################
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)
###########################
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df3)
##################
df3=df1.set_index('Courses').join(df2,set_index('Courses'),how='left')
print(df3)
###################
df3=df1.set_index('Courses').join(df2,set_index('Courses'),how='right')
print(df3)
########################
#pandas merging of DataFrame
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)

df3=pd.merge(df1,df2)
#########################
#use pandas.concat() to concat two dataframe
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900]})
data=(df,df1)
df2 = pd.concat(data)
df2
##########################
#columns are not maching
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark", "PySpark", "Python", "Pandas"],
                    'Fee' : ['20000', '25000', '22000', '24000']}) 
  
df1 = pd.DataFrame({'Courses': ["Unix", "Hadoop", "Hyperion", "Java"],
                    'Fee': ['25000', '25200', '24500', '24900']})
  
df2 = pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                    'Discount':[1000,2300,2500,2000,3000]})

df3=pd.concat([df,df1,df2])
print(df3)
#########################
23-02-26
#using numpy 
#arrays in numpy
#Create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)#output[10 20 30]
#################
#create a multi-dimensional Array
arr =np.array([[10,20,30],[40,50,60]])
print(arr)
#Represent the minimum dimensional Array
#use ndmin parameter to specify how many minimum
#dimension you wanted to create an array with 
#minimum dimension
arr = np.array([10,20,30,40],ndmin=3)
print(arr)
#three dimensional array
#####################
#change the Data type
#dtype parameter
arr = np.array([10,20,30,40],dtype= complex)
print(arr)
#####################
#get dimension of an array
arr =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)
#output
#2 dimension
###########################
#finding the size of each item in the array
arr = np.array([10,20,30])
print("Each item contain in bytes:",arr.itemsize)
##########
arr = np.array([[10,20,30,40],[50,60,70,80]])
print("Array size:",arr.size)
print("shape:",arr.shape)
################
arr = np.array([[10,20,40],[30,40,50]],dtype ='float')
print("Array created by using list:\n",arr)
##############3
#Arrange indexing in numpy
arr = np.arange(0,20,3)
print("A sequential array with steps of3:\n",arr)
#################
arr = np.arange(11)
print(arr)

print(arr[2])#2

print(arr[-2])#9
################
#multi dimensional Array 
#indexing array 
arr = np.array([[10,20,30,40,50],[50,30,20,10,30]])
print(arr)

print(arr.shape)

print(arr[1,1])

print(arr[0,4])

print(arr[1,-1])
#####################
# Acess array element using slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x = arr[1:8:2 ]#start:end:in step of 2
print(x)
#output[1,2,5,7]
#Example
x =arr[-2:3:-1]#start last but once(-2 )upto 3 but not 3 in step off
print(x)
#output[8,7,6,5,4]

x=arr[-2:10]#start last but once(-2)upto 10 but not 10 in step off
print(x)
#output[8,9]
##################
#multiple slicing
import numpy as np
multi_arr=([[10,20,10,40],
           [40,50,70,90],
           [60,10,70,80,],
           [30,90,40,30]])
multi_arr
#slicing array
print(multi_arr [1, 2])
multi_arr[1,:]
multi_arr[:,1]
x=multi_arr[:3, ::2]
print(x)
#############
import numpy as np
#integer array indexing
arr = np.arange(35).reshape(5,7)
print(arr)

#boolean Array indexing
import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)
#[[ 0  1  2  3]
#[ 4  5  6  7]
#[ 8  9 10 11]]

rows =np.array([False,True,True])
rows
wanted_rows= arr[rows, :]
print(wanted_rows)
#[[ 4  5  6  7]
# [ 8  9 10 11]]
##########################
#convert numpy into python list
array = np.array([10,20,30,40])
print("Array:",array)
print(type(array))

lst=array.tolist()
print("list:",lst)
print(type(lst))
###################
#convert multi-dimensional Array to list
array = np.array([[10,20,30,40,],
                 [50,60,70,80],
                 [60,40,20,10]])
print("Array:",array)

lst= array.tolist()
print("list:",lst)
###################
#reverse
list =[20,40,60,80]
array= np.asarray(list)
print("Array:",array)
print(type(array))
################
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
print(array.ndim)
print(array.itemsize)
print(array.size)
print(array.dtype)
########################
array = np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
#[[10 20]
 #[30 40]
 #[50 60]]
############
array= np.array([[10,20,30],[40,50,60]])
new_array= array.reshape(3,2)
print(new_array)
###############
24-02-26
#Arithmatic Operation (matrices manupulation)
import numpy as np
#1.Square_matrix(same number of rows and columns)
square_matrix = np.array([[1,2],[3,4]])
print("1.Square Matrix:\n",square_matrix)

#2.rectangular matrix(rows!=column)
rect_matrix=np.array([[1,2,3],[4,5,6]])
print("\n2.Rectangular Matrix:\n",rect_matrix)

#3.Diagonal matrix(non zero elements onli on main diagonal)
diagonal_matrix =np.diag([10,20,30])
print("\n3.Diagonal Matrix:\n",diagonal_matrix)
#4.scalar matrix (diagonal matrix with equal diagonal elements) 
scalar_matrix =np.diag([5,5,5])
print("\n4.Scalar matrix:\n",scalar_matrix)
#5.identity matrix(is on diagonal ,0s elesewhere)
identity_matrix = np.eye(3)
print("\n5 Identity Matrix:\n",identity_matrix)
#6.zero matrix (all elements are 0)
zero_matrix = np.zeros((3,3))
print("\n6.Zero Matrix:\n",zero_matrix)
#7.ones matrix(all elements are one)
ones_matrix = np.ones((3,3))
print("\n7 Ones Matrix:\n",ones_matrix)
#8.upper triangular matrix(zeros below diagonal)
upper_triangular = np.array([[1,2,3],
                             [0,4,5],
                             [0,0,6]])
print("n\8. Upper Triangular Matrix:\n",upper_triangular)
#9.lower triangular matrix(zeros above diagonal)
lower_triangular = np.array([[1,0,0],
                             [2,3,0],
                             [4,5,6]])
print("\n9. Lower Triangular Matrix:\n",lower_triangular)

#10.symmetric matrix(matrix == transpose)
symmetric_matrix = np.array([[1,7,3],
                             [7,4,-5],
                             [3,-5,6]])
print("\n10. Symmetric Matrix:\n",symmetric_matrix)
#11. skew-symmetric matrix(matrix ==-transpose)
skew_symmetric = np.array([[0,2,-1],
                           [-2,0,-4],
                           [1,4,0]])
print("\n11.Skew Symmetric Matrix:\n",skew_symmetric)
#12.Sparse Matrix (many zero entries)
sparse_matrix= np.array([[0,0,0],
                         [0,9,0],
                         [0,0,0]])
print("\n12.Sparse Matrix:\n",sparse_matrix)

#13.row matrix(1 row n columns)
row_matrix = np.array([[1,2,3]])
print("\n13.Row matrix:\n",row_matrix)
#14.column matrix(n rows 1 column)
column_matrix = np.array([[1],
                          [2],
                          [3]])
print("\n13. Column Matrix:\n",column_matrix)
#15.singleton matrix(1x1 matrix)
singleton_matrix = np.array([[42]])
print("\n15. Singleton Matrix:\n",singleton_matrix)
###########################
#matrix Addition
A =np.array([[1,2],[3,4]])
B =np.array([[5,6],[7,8]])
addition=A+B
print("\n Matrix Addition:\n",addition)
#matrix Subtraction
subtraction = A-B
print("\n Matrix Subtraction:\n",subtraction)

#scalar multiplacation
scalar_mult = 2*A
print("\n Scalar Multiplication:\n",scalar_mult)
#matrix multiplication(not product)
matrix_mult = np.dot(A,B)
print("\n Matrix Multiplication(Dot product):\n",matrix_mult)
#########################
#Transpose
transpose_A =A.T
print("\n Transpose of A:\n",transpose_A)
#determinant
det_A = np.linalg.det(A)#(linear algebra.determinent)
print("\n Determinant of A:\n", det_A)
#inverse
if np.linalg.det(A) != 0:
    inverse_A = np.linalg.inv(A)
    print("\n Inverse of A:\n",inverse_A)
else:
    print("\n Matrix A is singular (no inverse).")
################################
#trace(only applicable for matrices)
A
trace_A = np.trace(A)
print("\n Trace of A:\n",trace_A)

#eigenvalues and eigenvectors
eig_vals, eig_vecs = np.linalg.eig(A)
print("\n Eigenvalues of A:\n",eig_vals)
print("\nEigenvectors of A:\n",eig_vecs)
#########################