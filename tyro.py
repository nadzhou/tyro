from Bio import SeqIO
import numpy as np 

from sklearn.svm import SVC

def main(): 
    file_path = "apobecs_psi.fa.txt"
    seq_record = retrieve_seq(file_path)
    
    tyr_list = []
    for record in seq_record: 
        is_tyr = get_tyr_weights(record.seq)
        if is_tyr: 
            tyr_list.append(is_tyr)

    tyr_np = np.array(tyr_list)
    sulfation = check_sum(tyr_np)

    svm_clf = SVC(C=2, kernel="linear")
    svm_clf.fit(tyr_np, sulfation)
    test = tyr_np[2].reshape(1, -1)
    print(test)

    print(svm_clf.predict(test))


def retrieve_seq(file_path): 
    """Use Biopython to get input sequences as fasta."""
    return list(SeqIO.parse(file_path, "fasta"))


def get_tyr_weights(seq): 
    """Check if tyrosine is available, then encode and get weights for tyrosine stretches"""
    if "Y" in seq: 
        weighted_str = []
        tyr_index = seq.index("Y")

        stretch = str(seq[tyr_index - 5 : tyr_index + 5])
        ord_list = _encode_to_int(stretch)
        _get_residue_weights(ord_list, weighted_str)
        
        return weighted_str


def _encode_to_int(stretch):
    """Return the integer values for each character in the sequence."""
    return [ord(char) for char in stretch]


def _get_residue_weights(encoded_str, weighted_str): 
    """For each tyrosine stretch give weights to Q, D and Y as 1, otherwise -0.2"""
    required_values = [68, 69, 68]

    for char in encoded_str: 
        if char in required_values: 
            weighted_str.append(1)

        if char not in required_values: 
            weighted_str.append(-0.2)

    return weighted_str


def check_sum(np_array): 
    """Iteratively check whether each row sums to greater than 0 or less than 0."""
    return np.apply_along_axis(_check_sum, 1, np_array)


def _check_sum(array): 
    """If values sum greater than 0, it's a site of possible sulfation otherwise not."""
    if np.sum(array) > 0: 
        return "sulfation"

    if np.sum(array) < 0: 
        return "no sulfation"


if __name__ == '__main__': 
    main()