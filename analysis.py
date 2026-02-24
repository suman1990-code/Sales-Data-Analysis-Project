# python code to load Data

import  pandas as pd
df = pd.read_csv("D:/Data_Analystics_Project/sales_data_200rows.csv")

print(df)
print(df.head())

# 1. Total Sales

total_sales = df["Total_Sales"].sum()
print("Total Sales is :", total_sales)

# 2. Top Product

top_product = df["Product"].value_counts()
print("Top Product will be:",top_product)

# 3. max_Sales by City

max_sales by city = df.groupby("City")["Total_Sales"].sum()
print("The city wise max sale:",max_sales by city)

# 4. Highest Sales

highest_sale = df.sort_values("Total_Sales",ascending=False)
print("Highest sale is", highest_sale)

# 5. Average Sales

average_sale = df["Total_Sales"].mean()
print("Average Sale is :")
