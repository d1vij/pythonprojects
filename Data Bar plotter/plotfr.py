'''Reads data from graphingdata.txt and plots it'''
'''                requies ^ file to work'''

#generate list from responses
#responses=np.array([x.strip("\n") for x in file.readlines()])
#graph testing
#y axis has frequencies
#x has numbers
#logged till col 41 l log after that
import matplotlib.pyplot as plt
#import numpy as np
#5,3,7,9,7,9,4,8,3,3,3,3,7,3,8,7,2,9,2,3,3,7,7,3,3,7,7,7,4,7,2,1,3,4,5,6,7 <-till 41



#file i
file=open("graphingdata.txt","r")
f="".join(line for line in file.readline())
og=list(f.split(","))  

#count frequencies of numbers
count={}
for i in og :
    if i in count:
        count[i]+=1

    else:count[i]=1
print(count)


if "\n" in count : count.pop("\n")
#sort the keys from 'count' dict and create a new dict with the sorted keys
newkeys=sorted(count.keys())
newdict={i:count[i] for i in newkeys}

plt.bar([x for x in newdict.keys()],[y for y in newdict.values()])
plt.show()
