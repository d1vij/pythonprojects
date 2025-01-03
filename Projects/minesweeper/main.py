#main file
from functions import *

"""
-> a cli based minesweeper game
download all 3 files and simply run main.py
"""
def main():

    #initialization
    GRID = initialize_grid()
    GRID.display_stats()
    GRID.print_grid() #initial printing


    while True:
        # valid commands -> reveal | flag
        action = input("Input action (reveal | flag | unflag) \n>" ).lower().strip(' ')
        eol()
        match action:
            case "reveal": GRID.reveal_cell(get_coordinates_to(GRID, "reveal"))
            case "flag" : GRID.flag_cell(get_coordinates_to(GRID,"flag"))
            case "unflag" : GRID.flag_cell(get_coordinates_to(GRID,"unflag"))
            case "exit" | "quit" : GRID.end_game("bye")
            case _: print("invalid action") ; eol()
        GRID.print_grid()
        GRID.display_stats()


main()
