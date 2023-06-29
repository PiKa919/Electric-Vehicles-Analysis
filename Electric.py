#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('Electric_Vehicle_Population_Data copy.csv')


# In[4]:


#Check the structure and contents of the dataset using 
print(df.head())
df.info()


# In[6]:


#Examine summary statistics using
df.describe()


# In[8]:


#Check for missing values with
df.isnull().sum()


# In[ ]:




