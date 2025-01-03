import random



class Grid: # controls the overall grid
    def __init__(self,rows, columns, mineCount):
        self.rows = rows
        self.columns = columns
        self._mine_count = mineCount
        self._grid = [ [Cell(ro,col) for col in range(columns)] for ro in range(rows)]


    def setSurroundingMineCount(self) -> None:
        for eachRow in self._grid:
            for cell in eachRow:
                if not cell.is_mine:
                    change_by = [(-1, -1), (0, -1), (1, -1),
                                 (-1, 0), (1, 0),
                                 (-1, 1), (0, 1), (1, 1)]
                    count = 0
                    for dr, dc in change_by:
                        nr = cell.r + dr  # new row = cur row + change
                        nc = cell.c + dc  # new col = cur col + change

                        if nr in range(0, self.rows) and nc in range(0, self.columns):
                            if self._grid[nr][nc].is_mine : # == True
                                count += 1

                    cell.adj_mine_count = count


    def print_grid(self):
        print("- " * self.columns)
        for row in self._grid:
            for cell in row:
                print(cell,end="  ")
            print() # print newline
        print(" - " * self.columns)

    def placeMines(self):
        while self._mine_count > 0:

            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.columns - 1)

            if not self._grid[r][c].is_mine: #if - is not a mine | should be not false
                self._grid[r][c].is_mine = True
                self._mine_count -= 1


    def reveal_cell(self,cooridnates : tuple):
        row = cooridnates[0]
        column = cooridnates[1]
        cell = self._grid[row][column] #intitial target mine
        if cell.is_mine:
            cell._is_revealed = True
            end_game(f"mine encountered at{row + 1} : {column + 1}")
        else :
            cell.reveal(self._grid, self.rows, self.columns)






#===============================================================================================#



class Cell: # controls each indivisual space / block / box on the grid
    def __init__(self,rowValue : int, columnValue : int ):
        self.r = rowValue
        self.c = columnValue
        self.is_mine : bool = False
        self.adj_mine_count : int = 0
        self._is_revealed : bool = False
        self._is_flagged : bool = False

    # def reveal(self):
    #     # if self is mine and not revealed -> reveal self -> end game
    #     # else if  flagged -> print "cannot reveal current square - is flagged"
    #     # else if not revealed -> self._is_revealed = true
    #
    #     if not self._is_revealed and self.is_mine :
    #         self._is_revealed = True
    #         end_game(f"Mine encountered at {self.r + 1} : {self.c}")
    #     elif self._is_flagged :
    #         print(f"cannot reveal cell at {self.r} : {self.c} -> cell is flagged")
    #     elif not self._is_revealed :
    #         if self.adj_mine_count == 0 :
    #             self._is_revealed = True
    #             self.reveal_adj(self.r, self.c)
    #         else:
    #             self._is_revealed = True
    #     pass

    def reveal(self,grid : list, rows , columns):
        ...
        #TODO If the clicked cell's surrounding mine count
        # (adj_mine_count) is 0, the game automatically reveals all its neighboring cells.
        # This process repeats for any neighboring cell that also has a mine count of 0.

        if self.is_mine : return
        if self._is_flagged :
            print(f"You cannot reveal a flagged cell !!{self.r+1} : {self.c+1}")
            return
        if not self._is_revealed and not self._is_flagged:
            self._is_revealed = True
            if self.adj_mine_count == 0: # recursively reveal surroudning cells
                change_by = [(-1, -1), (0, -1), (1, -1),
                             (-1, 0), (1, 0),
                             (-1, 1), (0, 1), (1, 1)]
                for dr, dc in change_by:
                    nr = self.r + dr
                    nc = self.c + dc
                    if nr in range(0,rows) and nc in range(0,columns) :
                        grid[nr][nc].reveal(grid, rows, columns)


    def toggle_flag(self):
        self._is_flagged = not self._is_flagged # negation to flagged status


    def __str__(self): # to printout self status
        if self.is_mine and self._is_revealed : return "M"
        if not self._is_revealed : return "X"
        if self._is_revealed : return str(self.adj_mine_count)
        if self._is_flagged : return "?"





# GRID = Grid(5,5,5)
# GRID.placeMines()
# GRID.setSurroundingMineCount()
# GRID.print_grid()
# GRID.reveal_cell(1,1)
# GRID.print_grid()

def end_game(code : str = "None"):
    print(code)



"""

"""

















