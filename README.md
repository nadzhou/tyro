# tyro - Sample code for predicting tyrosulfation sites 

This is a sample code for predicting whether a given sequence may have potential for tyrosulfation. 

## Working 
The logic is pretty simple: 
  1. Find a position in a sequence where a tyrosine is located
  1. Take stretches that are 5 residues upstream and 5 residues down
  1. Convert the strings into integers and do a checksum 
  1. Residues that are not Q, D or Y are given -0.2 value while these three residues get +1
  
  1. Decide whether sulfaiton can happen or not, by check-summing the numpy ndarray. 
  
## Installation 
Just run 

```
  $ pip install -r requirements.txt
  
  $ python tyro.py
 ```
