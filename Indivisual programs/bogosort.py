import sys
sys.setrecursionlimit(10000000)
import random
iterations=0
def issorted(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:continue
        else:return False
    return True         

def bogosort(l):
    global iterations
    iterations+=1
    random.shuffle(l)
    if issorted(l):print(f"the array was sorted after {iterations} attempts)")
    else:
        print(l)
        print(iterations)
        bogosort(l)
l=[1,2,3]   #input list here (sorted or unsorterted) 
bogosort(l)