import unittest
from seq_read import ParseSeq
import numpy as np
from manipulate_tyro import TyroManipulate

class TestTyro(unittest.TestCase): 
    
    @classmethod
    def setUpClass(cls): 
        file_dir = "../apobecs_psi.fa.txt"
        cls.apobec_seqs = ParseSeq(file_dir, "fasta")
        cls.tyro = TyroManipulate(["A", "C", "T", "Y"]) 


    def test_read_seq(self): 
        apobec_name = "NP_001635.2"
        self.assertTrue(self.apobec_seqs.contains(apobec_name))


    def test_encode2int(self): 
        required_encoded = np.array([65, 67, 84, 89])

        self.assertEqual(self.tyro.encode2int().all(), required_encoded.all())


    def test_give_weights(self): 
        result = [-0.2, -0.2, -0.2,  1]

        self.assertEqual(result, self.tyro.give_weights().tolist())


if __name__ == "__main__": 
    unittest.main()