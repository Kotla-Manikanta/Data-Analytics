import pandas as pd
# s=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print(s)


data={
    'name':['kmk','mani','nav'],
    'age':[25,22,23],
    'city':['mbnr','jcl','hyd']
}
df=pd.DataFrame(data)
# print(df)

# print(df.head())
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)

# print(df['age'])
# print(df[['age','city']])
# print(df['age']>22)
# print(df.iloc[1])

# df['age']+=1
# print(df)

# df['age']=39
# print(df)

# df.rename(columns={'age':'years'},inplace=True)
# print(df)

df.drop('city',axis=1,inplace=True)
print(df)