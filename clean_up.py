view_file = "visited_products.csv"
purchased_file = "purchased_products.csv"
products_file = "catalog_items.csv"

products = None
with open(products_file, "r") as file:
    products = file.readlines()[1:]
    
print("Load products")


removed = 0
with open(purchased_file, "r") as in_file:
    with open("cleaned-"+purchased_file, "w") as out_file:
        output_string=in_file.readline()
        line = in_file.readline()
        while line != "":
            if line.split(",")[1] in products:
                output_string += line
            else:
                removed += 1
            line = in_file.readline()
        
        out_file.write(output_string)

print(f"Cleaned purchase file, removed ${removed} entries")


removed = 0
with open(view_file, "r") as in_file:
    with open("cleaned-"+view_file, "w") as out_file:
        output_string=in_file.readline()
        line = in_file.readline()
        while line != "":
            if line.split(",")[1] in products:
                output_string += line
            else:
                removed += 1
            line = in_file.readline()
        
        out_file.write(output_string)

print(f"Cleaned visited file, removed ${removed} entries")


print("FINISHED")