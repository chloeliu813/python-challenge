#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import numpy as ny

file = "Resources/election_data.csv"
df_orig = pd.read_csv(file, delimiter = ',')
df_orig.head()


# In[2]:


#The total number of votes cast
A_Votes = df_orig['Voter ID'].count()
A_votes2 = A_Votes.astype('int32')

Summery_Votes = pd.DataFrame({"Total Number of Votes": [A_votes2]})
Summery_Votes


# In[3]:


#A complete list of candidates who received votes
B_Grouped = df_orig.groupby(['Candidate'])
B_Count = B_Grouped['Voter ID'].count()
Summery_Count = pd.DataFrame({"Candidates who got votes":[B_Count]})


# In[4]:


#The percentage of votes each candidate won
Sum = A_Votes


# Creating a new DataFrame using both duration and count
summary_table = pd.DataFrame({"Number of Votes": B_Count,
                                    "Percentage": (B_Count/Sum) * 100})
summary_table.head()


# In[5]:


Winner = summary_table.loc[summary_table['Percentage'].idxmax()]
Winner


# In[6]:


summary_table.to_csv("PyPoll_Answer.csv")
#do open cammand and add the others (with open command)

#The total number of votes cast
#A_votes

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#summary_table


#The winner of the election based on popular vote.
#Winner


# In[7]:


def write_and_print(file, text):
 file.write(text)
 print(text)
    
    
# and here is an example of calling write_and_print
with open("PyPoll_Answer.csv", "a") as file:
    file.write("\n\n The winner if the poll is")  
    Winner.to_csv(file, header=True)
    
    file.write(f"\n\n The total number if votes is")  
    Summery_Votes.to_csv(file, header=True)
    
    file.write(f"\n\n These are the candidates that got votes")  
    Summery_Count.to_csv(file,header=False)


# In[ ]:




