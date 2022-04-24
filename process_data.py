import pandas as pd
import numpy as np

users = pd.read_csv("target_group.csv")
catalog = pd.read_csv('catalog_items.csv')
visited = pd.read_csv('visited_products.csv')
purchased = pd.read_csv("purchased_producs.csv")

users.set_index("customer_id", inplace=True)

for i in range(65, 91):
    users[chr(i)] = 0
    

catalog.set_index("product_id", inplace=True)
catalog["bought"] = 0
catalog["visited"] = 0


for index, row in purchased.iterrows():
    try:
        catalog.loc[row["product_id"], "bought"] += 1
    except:
        pass
    try:
        users.loc[row["customer_id"], catalog.loc[row["product_id"], "category"]] += 1
    except:
        pass

print("PROCESSED PURCHASED")
    
for index, row in visited.iterrows():
    try:
        catalog.loc[row["product_id"], "visited"] += 1
    except:
        pass
    try:
        users.loc[row["customer_id"], catalog.loc[row["product_id"], "category"]] += 1
    except:
        pass
    
print("PROCESSED VISITED")
    

catalog.to_csv('product_buy-open.csv')
users.to_csv('users_fav-category.csv')

print("DONE")