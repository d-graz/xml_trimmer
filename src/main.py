from trimmer import Trimmer
import sys

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print("Error")
    print("Printing usage:")
    print("python main.py <source/file.xml> <output/file.xml> [#_of_articles]")
    sys.exit(-1)
elif len(sys.argv) == 3:
    trimmer = Trimmer(sys.argv[1],sys.argv[2],5000)
else:
    trimmer = Trimmer(sys.argv[1],sys.argv[2],sys.argv[3])
trimmer.trimm_and_clean()