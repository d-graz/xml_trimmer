def parse(file_in,file_out):
    file_original = open(file_in,"r")
    file_mod = open(file_out, "w")
    database_line = file_original.readlines()
    for line in database_line:
        for i in range(len(line)):
            if line[i] == ">" and line[i+1]=="<":
                file_mod.write(line[i])
                file_mod.write("\n")
            elif line[i] == "&":
                file_mod.write("e")
            else:
                file_mod.write(line[i])

