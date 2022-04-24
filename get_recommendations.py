import pandas as pd
import numpy as np
import requests, json

user_fav = pd.read_csv("users_fav-category.csv")
product_stats = pd.read_csv("product_buy-open.csv")
purchased_producs_file = "purchased_producs.csv"
target_troup_file = "target_group.csv"


body = {}

purchases = {}

with open(purchased_producs_file, "r") as file:
    lines = file.readlines()[1:]
    for line in lines:
        line = line.strip().split(",")
        if line[0] not in purchases:
            purchases[line[0]] = []
        time = line[2]
        time = time[:time.index("+")]
        purchases[line[0]].append({
            "game": line[1],
            "time": time
        })

with open(target_troup_file, "r") as file:
    lines = file.readlines()[1:]
    for line in lines:
        uid = line.strip()
        if uid not in purchases:
            purchases[uid] = []
        body[uid] = [ x["game"] for x in purchases[uid]]
        

owned_products = body

sorted_products = {}
for char in range(65, 91):
    sorted_products[chr(char)] = product_stats.loc[product_stats['category'] == chr(char)].sort_values(["bought", "visited"], ascending=[False, False])

recommendations = ["customer_id,product_id"]
for index, row in user_fav.iterrows():
    user_id = row[0]
    s_categories = [[chr(x+65), row[x+1]] for x in range(26)]
    s_categories.sort(key = lambda x:x[1], reverse = True)
    
    cnt = 0
    while cnt < 5:
        for category in s_categories:
            for prodct in sorted_products[category[0]]["product_id"]:
                if prodct not in owned_products[user_id]:
                    if cnt < 5:
                        recommendations.append(user_id+","+prodct)
                    cnt += 1
                    
        
print("WRITING")
with open("output_file.csv", "w") as file:
    file.write("\n".join(recommendations))
print("DONE")