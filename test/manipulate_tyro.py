from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np 


class TyroManipulate: 
    def __init__(self, sequence): 
        self.sequence = np.array(sequence)
        self.encoded = None 



        if self.encoded == None: 
            self.encoded = self.encode2int()



    def encode2int(self):
        return np.array([ord(char) for char in self.sequence])


    def give_weights(self): 
        important_ordinals = [68, 69, 89]
        self.encoded = np.where(np.isin(self.encoded, important_ordinals), 1, self.encoded)
        
        return np.where(self.encoded != 1, -0.2, self.encoded)