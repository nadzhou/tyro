import unittest
from seq_read import ParseSeq


class TestTyro(unittest.TestCase): 
    
    @classmethod
    def setUpClass(cls): 
        file_dir = "../apobecs_psi.fa.txt"
        cls.apobec_seqs = ParseSeq(file_dir, "fasta")

    def test_read_seq(self): 
        apobec_name = "NP_001635.2"
        self.assertTrue(self.apobec_seqs.contains(apobec_name))





if __name__ == "__main__": 
    unittest.main()