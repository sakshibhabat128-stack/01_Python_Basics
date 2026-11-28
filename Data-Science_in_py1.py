# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 17:05:48 2026

@author: YADNYESH
"""
#import required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
#---------------------------------------------------
#load the sample dataset
#---------------------------------------------------
tips = sns.load_dataset('tips')
#--------------------------------------------------------
#basic data understanding
#--------------------------------------------------------
tips.describe()#statistical summary of numeric columns
tips.head()#preview first few rows of the dataset
#---------------------------------------------------
#Distribution analysis
#---------------------------------------------------
#Distribution of total bill amounts
sns.displot(tips.total_bill)

#Distribution of total bill with KDE(kernel density Estimate)
sns.displot(tips.total_bill, kde=True)
#KDE(kernel density Estimation)shows a smooth estimates
#of the probability density function of the data
#interpretation
#the distribution is right skew(positively skewed)
#most total bill are concentrated at lower values 10$ to 25$
#A few very large bills stretch the tail to the right
#this is common in service /restraurant data:
#most customer spend moderately, a few spend heavily    
#Distribution of tip amount with kDE
sns.displot(tips.tip, kde=True)
#-----------------------------------------------------------
#BIVARIATE ANALYSIS-JOINT PLOTS
#-----------------------------------------------------------
#scattar plot marginal histogram
sns.jointplot(x=tips.tip, y=tips.total_bill)

#Scatter plot with regression line
sns.jointplot(x=tips.tip, y=tips.total_bill,kind='reg')
#interpratation
'''
joint plot interpretation

Center (Scatter Plot):
-Each point represent one customer visit
-x-axis:tip amount
- y-axis :total bill
-clear positive relationship
as total bill increases,tip generally increases

Regression line:
-shows overall trend
-relationship is positive but not perfectly linear
-variable increases for higher bills

top histogram(x-axis):
-distribution of tip values
-    
''' 
25-02-26
#Hexbin joint plot for density based visualization
sns.jointplot(x=tips.tip, y=tips.total_bill, kind='hex')
#-------------------------------------------------------- 
#PARIWISE RELATIONSHIP
#--------------------------------------------------------
sns.pairplot(tips, kind='reg')
'''
Pairplot Insights:
    
Total_bill vs tips:
-strong positive correlation
-higher bills generally receive higher tips

total_bill vs size:
-weak to moderate positive correlation
-larger groups tend to generate higher bills
-however, small group can also have high bills

tip vs size:
-weak correlation
-larger groups do not always  leave higher tips
-most tips still cluster around $2-$5
'''
#---------------------------------------
#PAIRPLOT WITH TIME(LUNCH VS DINNER)
#---------------------------------------    
sns.pairplot(tips, hue='time')
'''
Insights by time of Visit:
    
Distribution:
-Dinner bills are generally higher than lunch bills
-Dinner shows wider variability in total bill and tips
-Lunch bills are more concentrated at lower values

Group size:
-Dinner group tend to be larger
-Lunch group are mostly size 2

Relationship:
-Positive total_bill vs tip relationship exists for both
-Dinner shows more extreme(high bill,high tip)cases
''' 
#-----------------------------------   
#PAIRPLOT WITH DAY
#-----------------------------------
sns.pairplot(tips, hue='day')   
'''
Day-wise Insights:

Total Bill:
-Saturday shows highest spending and widest spread
-Friday has fewer observation and lower spending

Tip:
-Higher tips are more frequent on Saturday and Sunday
-thursday and Friday show fever high tips

Group Size:
-Most groups are size 2-3 across all days
-large groups(5-6) appear mostly on weekends
'''
#--------------------------------------------
# CORRELATION HEATMAP      
#--------------------------------------------
sns.heatmap(tips.corr(numeric_only=True),annot=True)
'''
Correlation Interpretation:
correlation values range from -1 to +1

total_bill & tip(~0.68):
-Strong positive correlation
-Larger bills generally lead to higher tips

total_bill &size(~0.68):
-Moderate positive correlation
-Larger group tend to order more

tip & size (~0.49):
-Moderate correlation
-Group size affects tips, but not as strongly as bill amount    
'''
#-------------------------------------
#BOXPLOTS-OUTLIER DETECTION
#--------------------------------------
sns.boxplot(tips.total_bill)
#shows several high-value outliners- very expensive meals

sns.boxplot(tips.tip)
#shows tip outliners - unusually high tips

#-----------------------------------
#COUNT PLOTS
#-----------------------------------

sns.countplot(x=tips.day)
#Most of customers are coming on sat and sun .there is considerable strength
#very few customer are coming on friday    

sns.countplot(x=tips.sex)
#More male customer than female customer

#---------------------------------------
#PIE & BAR CHARTS
#----------------------------------------

tips.sex.value_counts().plot(kind='pie', autopct='%1.1f%%')
tips.sex.value_counts().plot(kind='bar')

#------------------------------------
#TIME-WISE DAY ANALYSIS
#------------------------------------

sns.countplot(data=tips[tips.time=='Dinner'], x='day')
#Dinner is most popular on saturday and sunday

sns.countplot(data=tips[tips.time=='Lunch'],x='day')
#lunch occurs mostly on Thursday and Friday

#----------------------------------
#FACET GRID ANALYSIS
#----------------------------------

fg = sns.FacetGrid(tips, row='smoker', col='time')
fg.map(sns.histplot, 'total_bill')

'''
tips=dataset
row='smoker'=separate rows for:
smoker= Yes
smoker = No    
col='time'= separate columns for:
Lunch
Dinner
this creates a 2 x 2 grid (4 small plots)

FaceGrid Interpretation:
    
Panels:
-smokers vs Non-smokers
-lunch vs Dinner

observation:
-dinner time = higher revenue opportunity
-smoker tables bring higher bill
dinner customer
high-spending smoker groups
 ''' 
##############################################################  
#-------------------------------------------------------
#MATPLOTLIB IMPLEMENTATION (WITHOUT SEABORN PLOTS)
#-------------------------------------------------------
#histogram of total bill
plt.hist(tips['total_bill'],bins=20, edgecolor='black')
plt.title('Total Bill Distribution')
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.show()
#-----------------------------------
#KDE USING SCIPY
#-----------------------------------
data = tips['total_bill']

density = gaussian_kde(data)              #Fit KDE model
x= np.linspace(min(data),max(data),200)   #X-axis range
y = density(x)                            #Density values

plt.hist(data, bins=20, density=True, alpha=0.6,edgecollor='black')
plt.plot(x,y,linewidth=2)
plt.title("Total Bill Distribution with Density Curve")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()
#-------------------
#TIP DISTRIBUTION
#-------------------
26-02-26
plt.hist(tips['tip'], bins=20, edgecolor='black')
plt.title('Tip Distribution')
plt.xlabel('Tip')
plt.ylabel('Count')
plt.show()

#--------------------------------------------
#SCATTER PLOT
#--------------------------------------------
plt.scatter(tips['tip'],tips['total_bill'],alpha=0.6)
plt.title('Tip vs Total Bill')
plt.xlabel('Tip')
plt.ylabel('Total Bill')
plt.show()

#------------------------------------------
#CORRELATION MATRIX (MATPLOTLIB) Heat Map
#------------------------------------------
corr = tips.corr(numeric_only=True)
corr
plt.imshow(corr, interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns, rotation=45)
plt.yticks(range(len(corr)), corr.columns)
plt.title('Correlation Matrix')
plt.show()

#------------------------------------
#BOXPLOTS
#------------------------------------
plt.boxplot(tips['total_bill'])
plt.title('Boxplot - Total Bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('Boxplot - tip')
plt.show()

#----------------------------
#BAR & PIE CHARTS
#----------------------------
tips['day'].value_counts().plot(kind='bar')
plt.title('Count by Day')
plt.show()

tips['sex'].value_counts().plot(kind='bar')
plt.tile('Coount byGender')
plt.show()

tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()
