"""
#11/10/24
Pascals triangle
             1             
            1 1            
           1 2 1           
          1 3 3 1          
         1 4 6 4 1         
       1 5 10 10 5 1       
     1 6 15 20 15 6 1      
    1 7 21 35 35 21 7 1    
  1 8 28 56 70 56 28 8 1   
1 9 36 84 126 126 84 36 9 1


number of numbers in each nth row = 2n+1 {rows start from n=0}

binomial expansion  - summation nCr = nc0+nc1+nc2.....ncr { where r=n}


"""

row_counter=0
terms=0

output=[]

from math import factorial

def combination(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))
def row_n(rows): #generates every nth row of pascal triangle
    terms=0
    output.clear()
    while terms<=rows:    
        output.append(combination(rows,terms)) #output updation
        terms+=1
    print(output)
        

# body
rows=int(input("input range >> "))
for i in range(rows):
    row_n(i)

        


    



















