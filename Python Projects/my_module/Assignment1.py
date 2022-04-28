
import pandas as pd


import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

# To find the dimension of dataframe
print(df.shape)

df.info()

# Find Duplicate rows
duplicateDFRow = df[df.duplicated()]
print('Duplicate Row:%s'%duplicateDFRow.count())

age = df['age']
fare = df['fare']

# To find duplicate values in age and fare column
ageFare = df.duplicated(subset=['age','fare']).sum()

print(ageFare)

print('Age:%s'%age.value_counts())
print('Fare:%s'%fare.value_counts())

# to determine null value

print(df.isnull().any().any())

# Make table with only survived and gender

table = pd.crosstab(df['survived'],df['gender'])

print(table)

ticketTable = pd.crosstab(df['survived'],df['class'])

print(ticketTable)


male = df[df['gender'] == 'M']

print(male.value_counts())

female = df[df['gender'] == 'F']

print(female.value_counts())

classMaleFemale = pd.crosstab(df['gender'],df['class'])

print(classMaleFemale)

embarkment = pd.crosstab(df['embarked'],df['survived'])

print(embarkment)


maleSurvive = df.loc[(df['survived'] == 'yes') & (df['gender'] == 'M')]
print(len(maleSurvive))

df['gender'].value_counts().plot.bar(rot=0)