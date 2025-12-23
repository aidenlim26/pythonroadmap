import pandas as pd

df = pd.read_csv("titanic_passengers.csv")

#print(df.head()) #shows first 5 rows
#print(df.tail()) #shows last 5 rows
#print(df.sample()) #shows random 5 rows
#print(df.info)
print(df.describe())