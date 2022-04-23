# import pandas as pd
import json

view_file = "visited_products.csv"
purchased_file = "purchased_products.csv"
users_file = "target_group.csv"
products_file = "catalog_items.csv"

# users_dict = {}

# with open(users_file, "r") as file:
#     line = file.readline()
#     while line != "":
#         users_dict[line] = {}
#         line = file.readline()

pid_dict = {}

with open(products_file, "r") as file:
    file.readline()
    line = file.readline().split(",")
    while line != [""]:
        pid_dict[line[0]] = [0, 0] # visit, purchase
        line = file.readline().split(",")
        
print("Created product database")
        
with open(purchased_file, "r") as file:
    file.readline()
    line = file.readline().split(",")
    while line != [""]:
        if len(line) == 3 and line[1] in pid_dict:
            pid_dict[line[1]][1] += 1
        line = file.readline().split(",") 
        
print("Got purchases")  
             
# with open(view_file, "r") as file:
#     file.readline()
#     line = file.readline().split(",")
#     while line != [""]:
#         if len(line) == 3 and line[1] in pid_dict:
#             pid_dict[line[1]][0] += 1
#         line = file.readline().split(",")
        
# print("Get visits")

# pid_dict = {"a":[12, 10],"b":[4, 1],"c":[100, 50],}

sr = sorted(pid_dict.items(), key=lambda x: x[1], reverse=True)

print("Sorted")

with open("only_purchases-products.csv", "w") as outfile:
    outfile.write('\n'.join(e[0] for e in sr))
    
print("Write successful")
    
        

# with open("fase_2-products.json", "w") as outfile:
#     json.dump(pid_dict, outfile)
    
# print("Write")
