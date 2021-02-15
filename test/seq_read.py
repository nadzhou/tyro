from Bio import SeqIO
import numpy as np 
from typing import List

class ParseSeq(object): 
    def __init__(self, file_dir, format): 
        self.file_dir = file_dir
        self.format = format


    def read_seq(self) -> List: 
        """Read the sequences."""
        return list(SeqIO.parse(self.file_dir, self.format))


    def contains(self, item: List) -> bool: 
        for record in self.read_seq(): 
            if item in record.id: 
                return True

