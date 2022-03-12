import pandas as pd 
import numpy as np 
df = pd.read_csv('intelligentGuessingDataSet.csv' , encoding = 'latin1')
# print(df['Email Pattern'].head())

df['parts'] = [x.split('@')[0] for x in df['email']]
# print(df['parts'])

df['pract'] = df['parts'].str.split('.')





# df['prac'] =  df['firstname'].str[:1]+'.'+df['lastname']
# print(df['prac'])

conditions = [df['parts'] == df['firstname'].str.lower(),
			  df['parts'] == df['lastname'].str.lower(),
			  # df['parts'] == df['firstname'].str[:1]+'.'+df['lastname'].str[7:]
			  
			  ]

choices = ['<11>' , '<22>']

df['pattern'] = np.select(conditions, choices ,default = 'Tie')
print(df.head())