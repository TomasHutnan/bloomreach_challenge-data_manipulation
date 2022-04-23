view_file = "visited_products.csv"
purchased_file = "purchased_products.csv"
users_file = "target_group.csv"
products_file = "catalog_items.csv"

# sorted_products = "sorted_products.csv"

def get_sorted_products_by_purchases():
    pid_dict = {}
    
    with open(products_file, "r") as file:
        file.readline()
        line = file.readline().split(",")
        while line != [""]:
            pid_dict[line[0]] = [0, 0] # visit, purchase
            line = file.readline().split(",")
        
    print("Loaded products")
    
            
    with open(purchased_file, "r") as file:
        file.readline()
        line = file.readline().split(",")
        while line != [""]:
            if len(line) == 3 and line[1] in pid_dict:
                pid_dict[line[1]][1] += 1
            line = file.readline().split(",") 
            
    print("Loaded purchases")
    
            
    with open(view_file, "r") as file:
        file.readline()
        line = file.readline().split(",")
        while line != [""]:
            if len(line) == 3 and line[1] in pid_dict:
                pid_dict[line[1]][0] += 1
            line = file.readline().split(",")
            
    print("Loaded visits")
    
    kept_values = {}
    for key in pid_dict:
        if pid_dict[key][0] != 0 and pid_dict[key][1] != 0:
            kept_values[key] = pid_dict[key]
    
    pid_dict = kept_values
        
    print("Deleted value-less products")
    
    VISIT_MULTIPLIER = 0.5 # first
    PURCHASE_MULTIPLIER = 1 # second
    sr = sorted(pid_dict.items(), key=lambda x: x[1][1]*PURCHASE_MULTIPLIER + x[1][0]*VISIT_MULTIPLIER, reverse=True)

    print("Sorted")
    
    return [e[0] for e in sr]


def get_user_purchases():
    uid_purchases={}
    
    with open(users_file, "r") as file:
        file.readline()
        line = file.readline().strip()
        while line != "":
            uid_purchases[line] = []
            line = file.readline().strip()
            
    print("Loaded users")
            
    with open(products_file, "r") as file:
        file.readline()
        line = file.readline().split(",")
        while line != [""]:
            if len(line) == 3 and line[0] in uid_purchases and line[1] not in uid_purchases[line[0]]:
                uid_purchases[line[0]].append(line[1])
            line = file.readline().split(",")
            
    print("Loaded purchases")
            
    return uid_purchases
        

product_leaderboard = get_sorted_products_by_purchases()
user_purchases = get_user_purchases()


with open("recommendations-purchasesX1+viewsX0.5.csv", "w") as file:
    file.write("customer_id,product_id\n")
    for user in user_purchases:
        recommended = 0
        i = 0
        while recommended < 5 and i < 112561:
            if product_leaderboard[i] not in user_purchases[user]:
                file.write(user+","+product_leaderboard[i]+"\n")
                recommended += 1
            i += 1
    
print("Written")
    
