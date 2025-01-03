from classes import *

def eol() -> None:
    print("-----------------------------------------------")


def get_difficulty():
    difficulty = input("Input difficulty <easy | med | hard | custom>  \n>").lower().strip()
    eol()
    match difficulty:
        case "easy":
            rows = 9; columns = 9; minecount = 10
        case "med":
            rows = 16; columns = 16; minecount = 40
        case "hard":
            rows = 30; columns = 16; minecount = 99

        case "custom":
            rows = 9; columns = 9; minecount = 10
        case _:
            print("input a valid difficulty !")
            initialize_grid()
    return rows,columns,minecount


def initialize_grid():
    grid = Grid(*get_difficulty()) # ' * ' operator for unpacking the returned tuple
    grid.placeMines()
    grid.setSurroundingMineCount()
    return grid

def get_action():
    action = input("Input action (reveal | flag)").lower().strip(" ")
    if action == "reveal" or action == "flag":return action
    else:print(f"invalid action {action}");get_action()


def get_coordinates_to(grid : Grid, action) :
    cor = input(f"Input the cell's coordinates to {action} (eg 1,2 <use comma>) \n>").split(',')
    eol()
    if len(cor) == 2:
        try :
            r: int = int(cor[0])
            c: int = int(cor[1])
        except TypeError:
            print("Only integral values are allowed")
            eol()
            get_coordinates_to(grid)

        if r-1 in range(0, grid.rows) and c-1 in range(0,grid.columns):
            return tuple([r - 1, c - 1])
        else:
            print(f"Invalid coordinates {r} : {c}")
            eol()
            get_coordinates_to(grid,action)

    else :
        print("invalid co-ordinates!")
        eol()
        get_coordinates_to(grid,action)
