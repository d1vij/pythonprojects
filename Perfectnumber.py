# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:32:07 2024

@author: Divij Verma




1. Write a Python function to check whether a number is "Perfect" or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper 
positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
Click me to see the sample solution




"""
print(1)

factors_=[]
def factors(number):
    for i in range(1,number):
        if number%i==0:
            factors_.append(i)

def isperfect(seq,number):
    if sum(factors_)==number:return True
    else:return False
    

number=int(input(">>"))
factors(number)
print(f"The number {number} is a perfect number ?{isperfect(factors_ , number)}")