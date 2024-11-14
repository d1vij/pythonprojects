#7up7down
import random
from time import sleep
selfnumber=0
roundnumber=0
userscore=0
userchoice=0




def game():
    global roundnumber
    global userscore
    roundnumber+=1
    userchoice=int(input("Input your choice : \n [1] 7 down \n [2] equals 7 \n [3] 7 up \n >>> "))
    selfnumber=random.choice([1,2,3,4,5,6,7,8,9,10])
    sleep(1)
    if userchoice==1:
        if selfnumber>=7:
            print(f"wrong guess , your choice : 7down , number was {selfnumber}")
        else:
            print("right guess")
            userscore+=1
    elif userchoice==2:
        if selfnumber!=7:print(f"wrong guess , your choice : 7 , number was {selfnumber}")
        else:
            print("right choice")
            userscore+=1
    else:
        if selfnumber<=7:print(f"wrong guess , your choice : 7up , number was {selfnumber}")
        else:
            print("right guess")
            userscore+=1

def showstats():
    print(f"====================\n your gamescore is {userscore}")
    print(f"you played a total of {roundnumber} rounds")
def ui():
    print("========================")
    userchoice=int(input("What do you want to do : \n [1] play another round \n [2] show stats  \n >>> "))
    if userchoice==1:game()
    elif userchoice==2:showstats()




while True:
    sleep(1)
    ui()
