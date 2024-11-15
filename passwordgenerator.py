import random
import numpy as np

pw = np.array([
    *[chr(i) for i in range(65, 91)],     
    *[chr(i) for i in range(97, 123)],  
    *[chr(i) for i in range(48, 58)], 
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
])

password=""
def initiate():
    pw.resize(1,92)
    random.shuffle(pw)
    pw.resize(23,4)
def getrand_mn():
    m=random.choice(range(23))
    n=random.choice(range(4))
    return m,n
def addvalue():
    global password
    m,n=getrand_mn()
    password+=pw[m][n]

def main_passgen():
    initiate()
    l=int(input("input length of password >>> "))

    for i in range(l):
            addvalue()
    print(f"your password is \n-=-=-=-=-=- \n {password} \n-=-=-=-=-=-")
      
    
    
