# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:31:51 2024

@author: Divij Verma
"""

#palindrome
l=list(input(">>"))


def is_palindrome(list):
    for i in range(len(l)//2):
        if (list[i]!=list[len(list)-i-1]):
            return False
            
    return True
        
            
if is_palindrome(l):print(f"{l} is a palindrome")
else:print(f"{l} is not a plaindrome")     
   
