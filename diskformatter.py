import random
file=open("checkfilesize.txt","wb")
for i in range(1000000):
    file.write(random.randbytes(1000000))