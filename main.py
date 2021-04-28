import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
temp = df.groupby('race/ethnicity')['reading score'].mean()

print(temp)
