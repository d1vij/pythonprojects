#generate random data
import random
size=int(input("INput data size :> "))
print(list(random.randint(1,10) for i in range(size)))