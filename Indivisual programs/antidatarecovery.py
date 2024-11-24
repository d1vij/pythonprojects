#fills {size} amount of disk space with random bytes
#this over writes on top of disk space which has been declared "free"
#by os which makes it impossible to recover 
#execution time increases significantly with increase in input size





import random
from math import pow
from os import remove
size=input("input your file size with suffix of (By , MB , GB) :> ")

    

    
def fillunfill(size_):
    global size
    match conversionfactor:=size_[-2:].lower():
        case "gb":conversionfactor=int(pow(10,9))
        case "mb":conversionfactor=int(pow(10,6))
        case "by":conversionfactor=1
        case _ :
            size=0
            
            print("enter a valid size !")
            return False
        
            
        
    sint=int(size_[:-2])
    file=open("tmpdf1.txt","wb")
  
    #write file
    for _ in range(sint*conversionfactor):file.write(random.randbytes(1))
    #delete file
    file.close()
    remove("tmpdf1.txt")
    
    
fillunfill(size) 
print(f"{size} of disk space has been made impossible to recover !")
exit()


