with open("purchased_producs.csv", "r") as inp:
    with open("output_file.csv", "w") as oup:
        line = inp.readline()
        oup.write(line+"\n")
        while line != "":
            line = inp.readline()
            oup.write(line[:84]+"\n")

print("DONE")
