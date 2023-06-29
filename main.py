import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Electric_Vehicle_Population_Data copy.csv')

# #Check the structure and contents of the dataset using 
# print(df.head())
# df.info()

# #Examine summary statistics using
# df.describe()

# #Check for missing values with
# df.isnull().sum()

df = df.drop('Legislative District', axis=1)
print(df.info())

