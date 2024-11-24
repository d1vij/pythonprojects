
"""
grocery list maker
>Continously inputs from user untill the user exits , and stores the input accordingly
"""

grocery_list={}
from time import sleep

def additem():  
    item=input("Input your item > ").lower().strip()
    if item in grocery_list:grocery_list[item]+=1
    else:grocery_list[item]=1
    askuser()
    
def outputlist():
    match input("How do you want to output your Grocery List\n "
                "------------\n"
                "[1]Print here\n"
                "[2]Output as text file\n"
                "--------------\n"
                ">>> "):
        case "1":
            #print in console
            print("------------\n"
                  "Item name -> quantity")
            output="\n".join(f"{itemname} ->  {qnt}" for itemname,qnt in grocery_list.items())
            print(output)
            #print("-----------------\n")
            sleep(1)
            askuser()
        case "2":
            file=open("grocerylist.txt",'a')
            for i in grocery_list:
                item_=f"{i} -> {grocery_list[i]}\n"
                file.write(item_)
                #file.write(f"{itemname} ->  {qnt}" for itemname,qnt in grocery_list.items())
            file.close()
            print("Your list is stored in the file *\grocerylist.txt")
            askuser()
            
def askuser():
    
    #ask user for operation
    match input("---------------\n"
                "What operation do you want to do ?\n"
                "----------------\n"
                "[1]Add new item\n"
                "[2]show list\n"
                "[3]quit\n"
                "----------------\n"
                ">>> "):
        case "1":
            additem()
        case "2":
            outputlist()
        case "3":
            return False 
        case _ :
            print("This input is not a valid choice !")
            askuser()
           
if __name__=="__main__":
    askuser()
        
