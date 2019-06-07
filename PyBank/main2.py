#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import csv
import numpy as np


# In[2]:


file = "budget_data.csv"

with open(file,newline='') as csvfile:
     csvreader = csv.reader(csvfile)
    
     for row in csvreader:
          print(row[0])

#file.head()


# In[3]:



df_orig = pd.read_csv(file, delimiter = ',')
df_orig.head()


# In[4]:


#The total number of months included in the dataset
A_Months = df_orig['Date'].count()
B = int(A_Months)


# In[5]:


#The net total amount of "Profit/Losses" over the entire period
B_ProfitLoss = df_orig['Profit/Losses'].sum()
print(B_ProfitLoss)


# In[6]:


#make a new column for change from previous number

# # create a differenced series
# def difference(dataset, interval=1):
#     diff = list()
#     for i in range(interval, len(dataset)):
#         value = dataset[i] - dataset[i - interval]
#         diff.append(value)
#     return Series(diff)

# # create a differenced series
# def difference(dataset, interval=1):
#     diff = list()
#     for i in range(interval, len(dataset)):
#         value = dataset[i] - dataset[i - interval]
#         diff.append(value)
#     return Series(diff)


# #difference_series = read_csv(file, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# X = df_orig['Profit/Losses'].values
# diff = difference(X)
# diff


# In[7]:


# # The average of the changes in "Profit/Losses" over the entire period
# def average(numbers):
#     length = len(numbers)
#     total = 0
#     for number in numbers:
#         total += number
#     return total/length

# print(average(df_orig['Profit/Losses']))

##
df_orig['Change'] = df_orig['Profit/Losses'] - df_orig['Profit/Losses'].shift(+1)
df_orig

avg_changePL = df_orig['Change'].mean()
avg_changePL


# In[8]:


#The greatest increase in profits (date and amount) over the entire period
D_Max = df_orig.loc[df_orig['Profit/Losses'].idxmax()]
print(D_Max)


# In[9]:


#The greatest decrease in losses (date and amount) over the entire period
E_Min = df_orig.loc[df_orig['Profit/Losses'].idxmin()]
print(E_Min)


# In[10]:



answer1 = pd.DataFrame({"Total Months": [B], "Total":[B_ProfitLoss]})
answer2 = pd.DataFrame({"Greatest increase in profits": [D_Max]})
answer3 = pd.DataFrame({"Greatest decrease in losses": [E_Min]}) 
answer4 = pd.DataFrame({"Average Change": [avg_changePL]})

#output_file = open("PyBank_Output.txt", "w")

with open("PyBank_Output.txt", "a") as file:
    file.write("\n Chloe's Answers \n\n")
    answer1.to_csv(file,header=True)
    file.write("\n\n")
    answer4.to_csv(file,header=True)
    file.write("\n\n")
    answer2.to_csv(file,header=True)
    file.write("\n\n")
    answer3.to_csv(file,header=True)


# In[ ]:




