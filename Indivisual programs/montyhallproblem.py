import random

def initiate_doors():
    doors = [0, 0, 0]
    car_at = random.randint(0, 2)
    doors[car_at] = 1
    return doors

def userchoice():
    try:
        match int(input("Input your choice of door (1,2,3) : ")):
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 2
            case _:
                return userchoice()
    except:
        return userchoice()

def main():
    doors = initiate_doors()
    user_door = userchoice()
    car_index = doors.index(1)
    door_with_goat = [x for x in range(len(doors)) if x != car_index and x != user_door]
    revealed_door = random.choice(door_with_goat)
    #print(doors)

    while True:
        switch = input(f"One goat is present in door {revealed_door+1}. \nDo you want to switch your door with the remaining door? (yes/no): ").lower()
        if switch in ["yes", "no"]:
            break
        print("Invalid input. Please type 'yes' or 'no'.")

    if switch == "yes":
        final_user_door = [x for x in range(len(doors)) if x != user_door and x != revealed_door][0]
    else:
        final_user_door = user_door

    if final_user_door == car_index:
        print(f"YOU WON THE CAR! It was behind door {car_index+1}!")
    else:
        print(f"You got the GOAT! The car was behind door {car_index+1}!")

while True:
    main()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
