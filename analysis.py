# python code to load Data

import  pandas as pd
df = pd.read_csv("D:/Data_Analystics_Project/sales_data_200rows.csv")

print(df)
print(df.head())

# 1. Total Sales

print(df["Total_Sales"].sum())

# 2. Top Product

print(df["Product"].value_counts())

# 3. Sales by City

print(df.groupby("City")["Total_Sales"].sum())

# 4. Highest Sales

print(df.sort_values("Total_Sales",ascending=False))

# 5. Average Sales

print(df["Total_Sales"].mean())