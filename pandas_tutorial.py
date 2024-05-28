import pandas as pd

"""
data = pd.read_csv("hw_200.csv")

filtered_data = data[data['Height(Inches)'] > 70]

grouped_data = data.groupby('Index')['Height(Inches)'].mean()

sorted_data = data.sort_values(by='Weight(Pounds)', ascending=False)

filtered_data.to_csv("filtered_data.csv", index=False) 

print(sorted_data)
"""

"""
data = pd.read_csv("homes.csv")

filtered_data = data[data['Taxes'] < 4000]

grouped_data = filtered_data.groupby('Rooms')['Sell'].mean()

sorted_data = filtered_data.sort_values(by='Age', ascending=False)

#sorted_data.to_csv("sorted_data.csv", index=False)

print(grouped_data)
"""

data = pd.read_csv("Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv")

grouped_data = data.groupby('Product')['Quantity Ordered'].sum()

print(grouped_data)