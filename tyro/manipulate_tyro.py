import numpy as np 


class TyroManipulate: 
    def __init__(self, sequence): 
        self.sequence = sequence
        self.encoded = None 

        if self.encoded == None: 
            self.sequence = self.seq2np()
            self.encoded = self.encode2int()


    def seq2np(self) -> np.ndarray:
        return np.asarray(self.sequence, dtype='S1')

    def encode2int(self) -> np.ndarray:
        """Encode the sequences into respective integers."""
        return self.sequence.view(np.uint8)


    def give_weights(self) -> np.ndarray: 
        """Ordinal values for aspartic acid, glutamic acid and tyrosine are given 1, otherwise -0.2"""
        important_ordinals = [68, 69, 89]
        self.encoded = np.where(np.isin(self.encoded, important_ordinals), 1, self.encoded)
        self.encoded = np.where(self.encoded != 1, -0.2, self.encoded)

        return self.encoded


    def check_sum(self) -> np.ndarray:   
        """Sum the array, if > 0, give 1 otherwise 0. A softmax-kind of function."""
        return np.apply_along_axis(self._check_sum, 1, [self.encoded])


    def _check_sum(self, array: np.ndarray) -> int: 
        """Softmax for 1 or 0."""
        if np.sum(array) > 0: 
            return 1
        return 0


