from tyro.parser import parse_args
from tyro.manipulate_tyro import TyroManipulate
from tyro.svm_classify import SulfoSVM
from tyro.seq_read import ParseSeq
from tyro.seq_read import ParseSeq

import sys
import numpy as np 
np.set_printoptions(threshold=sys.maxsize)
def main(): 
    seq_arg = parse_args()
    seq_obj = ParseSeq(seq_arg.input, seq_arg.format)

    seqs = seq_obj.tokenize()
    processed_seq = TyroManipulate(seqs)
    processed_seq.give_weights()
    print(processed_seq.encoded)    


    print(processed_seq.check_sum())








if __name__ == '__main__': 
    main()