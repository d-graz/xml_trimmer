class Trimmer:

    def __init__(self,reference,new,size):
        self.size = int(size)
        self.reference = reference
        self.new = new
        self.keywords = [["<article ","</article>\n"],["<inproceedings ","</inproceedings>\n"],["<proceedings ","</proceedings>\n"],["<book ","</book>\n"],["<incollection ","</incollection>\n"],["<phdthesis ","</phdthesis>\n"],["<mastersthesis ","</mastersthesis>\n"]]

    #def populate(self,keyword,reference_lines):
    #    new_file_size = 0
    #    for line in reference_lines:
    #        new_line = line.replace("&","e")
    #        if "</article>" in line and new_file_size == self.size-1:
    #            new_file.write("</article>")
    #            break
    #        elif "</article>" in line:
    #            new_file_size = new_file_size +1
    #            new_file.write(new_line)
    #        else:
    #            new_file.write(new_line)


    def trimm_and_clean(self):
        reference_file = open(self.reference, "r")
        new_file = open(self.new, "w")
        new_file.write("<dblp>\n")
        reference_lines = reference_file.readlines()
        for keyword in self.keywords:
            self.populate(keyword,reference_lines,new_file)
        reference_file.close()
        new_file.write("</dblp>")
        new_file.close()

    def populate(self,keyword,reference_lines,new_file):
        keyword_size = 0
        iteration = 0
        line_size = len(reference_lines)
        print(keyword)
        while keyword_size < self.size:
            while iteration<line_size and keyword[0] not in reference_lines[iteration]:
                iteration = iteration+1
            while iteration<line_size and keyword[1] != reference_lines[iteration]:
                #print("in loop whit :"+reference_lines[iteration])
                #string = reference_lines[iteration].replace("&","e")
                new_file.write(reference_lines[iteration])
                iteration = iteration +1
            if iteration<line_size:
                new_file.write(keyword[1])
            keyword_size = keyword_size+1
