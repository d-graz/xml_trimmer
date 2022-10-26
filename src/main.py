from trimmer import Trimmer
import database_cleaner as dbc
import sys


if len(sys.argv) < 2:
    print("Error")
    print("Specify action whit: clean,clean_csv,trim")
    sys.exit(-1)
if sys.argv[1] == "clean":
    if len(sys.argv) != 4:
        print("Error")
        print("Please specify input file and output file")
        sys.exit(-1)
    dbc.parse(sys.argv[2], sys.argv[3])
    sys.exit(0)
elif sys.argv[1] == "clean_csv":
    if len(sys.argv) != 4:
        print("Error")
        print("Please specify input file and output file")
        sys.exit(-1)
    dbc.parse(sys.argv[2], sys.argv[3],True)
    sys.exit(0)
elif sys.argv[1] == "trim":
    if len(sys.argv) == 4:
        trimmer = Trimmer(sys.argv[2],sys.argv[3],500)
    elif len(sys.argv) == 5:
        trimmer = Trimmer(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        print("Error")
        print("Please specify at least input file and output file")
        sys.exit(-1)
    trimmer.trim()
else:
    print("Error :"+sys.argv[1]+" not recognized")
    sys.exit(-1)