from Bio import SeqIO


class ParseSeq(object): 
    def __init__(self, file_dir, format): 
        self.file_dir = file_dir
        self.format = format

    def read_seq(self): 
        return list(SeqIO.parse(self.file_dir, self.format))


    def contains(self, item): 
        for record in self.read_seq(): 
            if item in record.id: 
                return True