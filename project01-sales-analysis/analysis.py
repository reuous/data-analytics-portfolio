import pandas as pd

df = pd.read_csv("/Users/reuous/Documents/GitHub/data-analytics-portfolio/project01-sales-analysis/train.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head())

df["Year"] = pd.to_datetime(df["Order Date"], dayfirst=True).dt.year
df = df.groupby("Year")["Sales"].sum().sort_values(ascending=False)
print(df)
