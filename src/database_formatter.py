import sys

def parser(file_name):
    file_original = open(file_name,"r")
    file_mod = open("modified_database.xml", "w")
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

if len(sys.argv)!=2:
    print("Error")
    sys.exit(-1)
parser(sys.argv[1])