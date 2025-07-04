import pandas as pd
# data = {"null":"","name":"krishna"}
# print(data)

#data frame
data =  {
     "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}
#df = pd.read_csv("ai_tool_popularity.csv")
#df = pd.read_csv("district wise rainfall normal.csv")

df = pd.DataFrame(data)
# print(df)
# print(df.info())
# print(df.head())
# print(df.shape)
# print(df.columns)

df['Age'] = df['Age'] + 1
print(df)
print(df[df['Age'] > 30])
