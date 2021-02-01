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
## Sample output 
Given an array of weight - which we got from a template Apobec protein sequence - the algorithm can predict whether these weights are a potential site for tyrosulfation or not. The output is as follows: 

![image](https://user-images.githubusercontent.com/25282805/106462230-9e25c400-64b7-11eb-882e-0b500fbbaa4b.png)
