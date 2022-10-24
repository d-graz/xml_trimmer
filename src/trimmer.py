class Trimmer:

    def __init__(self,reference,new,size):
        self.size = size
        self.reference = reference
        self.new = new

    def trimm_and_clean(self):
        reference_file = open(self.reference, "r")
        new_file = open(self.new, "w")
        reference_lines = reference_file.readlines()
        new_file_size = 0
        for line in reference_lines:
            new_line = line.replace("&","e")
            if "</article>" in line and new_file_size == self.size-1:
                new_file.write("</article>")
                break
            elif "</article>" in line:
                new_file_size = new_file_size +1
                new_file.write(new_line)
            else:
                new_file.write(new_line)
        reference_file.close()
        new_file.close()