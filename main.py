from classes import *

def initialize_grid():
    difficulty = input("Input difficulty <easy | med | hard | custom>").lower()
    match difficulty:
        case "easy": rows = 9 ; columns = 9 ; minecount = 10
        case "med":  rows = 16 ; columns = 16 ; minecount = 40
        case "hard": rows = 30 ; columns = 16 ; minecount = 99

        case "custom": rows = 9 ; columns = 9 ; minecount = 10
        case _:
            print("input a valid difficulty !")
            initialize_grid()

    grid = Grid(rows,columns,minecount)
    grid.placeMines()
    grid.setSurroundingMineCount()
    return grid
def main():

    #initialization
    GRID = initialize_grid()

    while True:
        # valid commands -> reveal | flag
        action = input("Input action (reveal | flag)")
        GRID.print_grid()
        GRID.reveal_cell(get_coordinates_to_reveal(GRID))

def get_coordinates_to_reveal(grid : Grid):
    cor = input("Input the cell's coordinates to reveal (eg 1,2 <use comma>) >").split(',')
    if len(cor) == 2:
        try :
            r = int(cor[0])
            c = int(cor[1])
        except TypeError:
            print("Only integral values are allowed")
            get_coordinates_to_reveal(grid)

        if r-1 in range(0, grid.rows) and c-1 in range(0,grid.columns):
            return r-1,c-1
        else:
            print(f"Invalid coordinates {r} : {c}")
            get_coordinates_to_reveal(grid)

    else :
        print("invalid co-ordinates!")
        get_coordinates_to_reveal(grid)

main()