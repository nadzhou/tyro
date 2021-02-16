import unittest
from seq_read import ParseSeq
import numpy as np
from manipulate_tyro import TyroManipulate
from svm_classify import SulfoSVM


def svm(): 
    tyro_sample = np.array([[-0.2, -0.2, -0.2,  1], 
                        [-0.2, -0.2, -0.2, -0.2], 
                        [-0.2, -0.2, -0.2, -0.2], 
                        [-0.2, 1, -0.2,  -0.2] ])
    sulfation = np.array([[1], 
                            [0], 
                            [0], 
                            [1]])

    return SulfoSVM(tyro_sample, sulfation, 0.5)


class TestTyro(unittest.TestCase): 

    @classmethod
    def setUpClass(cls): 
        file_dir = "../apobecs_psi.fa.txt"
        cls.apobec_seqs = ParseSeq(file_dir, "fasta")
        cls.tyro = TyroManipulate(["A", "C", "T", "Y"]) 
        cls.svm = svm()



    def test_read_seq(self): 
        apobec_name = "NP_001635.2"
        self.assertTrue(self.apobec_seqs.contains(apobec_name))


    def test_encode2int(self): 
        required_encoded = np.array([65, 67, 84, 89])

        self.assertEqual(self.tyro.encode2int().all(), required_encoded.all())


    def test_give_weights(self): 
        result = [-0.2, -0.2, -0.2,  1]

        self.assertEqual(result, self.tyro.give_weights().tolist())


    def test_checksum(self): 
        result = [1]
        self.assertEqual(self.tyro.check_sum(), result)

    def test_svm_classify(self): 
        expected = np.array([0.5, 0.5])
        self.assertEqual(self.svm.cros_validate().all(), expected.all())



if __name__ == "__main__": 
    unittest.main()