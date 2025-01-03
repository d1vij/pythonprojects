import random
import datetime

def eol() -> None:
    print("-----------------------------------------------")

class Grid: # controls the overall grid

    initialized_time = datetime.datetime.now()

    def __init__(self,rows, columns, mineCount):
        self.rows = rows
        self.columns = columns
        self._mine_count = mineCount
        self._grid = [ [Cell(ro,col) for col in range(columns)] for ro in range(rows)]
        self._remaining_cells = rows*columns
        self._flagged_cells = 0



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

    def display_stats(self):
        txt = f"Total rows -> {self.rows}\nTotal columns -> {self.columns}\nRemaining cells -> {self._remaining_cells}\nCurrently flagged cells -> {self._flagged_cells}\nMaximum flaggings allowed -> {self._mine_count}"
        print(txt)
        eol()

    def print_grid(self):
        self._flagged_cells = 0
        self._remaining_cells = 0
        # print("- " * self.columns)
        for row in self._grid:
            for cell in row:
                if not cell.is_revealed : self._remaining_cells += 1
                if cell.is_flagged : self._flagged_cells += 1
                print(cell,end="  ")

            print() # print newline

        eol()


    def placeMines(self):
        while self._mine_count > 0:

            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.columns - 1)

            if not self._grid[r][c].is_mine: #if - is not a mine | should be not false
                self._grid[r][c].is_mine = True
                self._mine_count -= 1


    def reveal_cell(self,coordinates : tuple):
        row = coordinates[0]
        column = coordinates[1]
        cell = self._grid[row][column] #intitial target mine
        if cell.is_mine:
            cell.is_revealed = True
            self.end_game(f"mine encountered at :> {row + 1} : {column + 1}")
            eol()
        else :
            cell.reveal(self._grid, self.rows, self.columns)

    def flag_cell(self, coordinates : tuple):
        row = coordinates[0]
        column = coordinates[1]
        cell = self._grid[row][column]
        if not cell.is_revealed :
            cell.toggle_flag()
        elif cell.is_revealed : print(f"Cannot flag a revealed cell :> {row+1} : {column + 1}") ; eol()

    @classmethod
    def end_game(cls,code: str = "None"):
        print(code)




class Cell: # controls each individual space / block / box on the grid
    def __init__(self,rowValue : int, columnValue : int ):
        self.r = rowValue
        self.c = columnValue
        self.is_mine : bool = False
        self.adj_mine_count : int = 0
        self.is_revealed : bool = False
        self.is_flagged : bool = False

    def reveal(self,grid : list, rows , columns):
        """If the clicked cell's surrounding mine count
        (adj_mine_count) is 0, the game automatically reveals all its neighboring cells.
        This process repeats for any neighboring cell that also has a mine count of 0."""

        if self.is_mine : return
        if self.is_flagged :
            print(f"You cannot reveal a flagged cell !!{self.r+1} : {self.c+1}")
            eol()
            return
        if not self.is_revealed and not self.is_flagged:
            self.is_revealed = True
            if self.adj_mine_count == 0: # recursively reveal surrounding cells
                change_by = [(-1, -1), (0, -1), (1, -1),
                             (-1, 0), (1, 0),
                             (-1, 1), (0, 1), (1, 1)]
                for dr, dc in change_by:
                    nr = self.r + dr
                    nc = self.c + dc
                    if nr in range(0,rows) and nc in range(0,columns) :
                        grid[nr][nc].reveal(grid, rows, columns)


    def toggle_flag(self):
        self.is_flagged = not self.is_flagged # negation to flagged status


    def __str__(self): # to printout self status
        if self.is_flagged : return "?"
        if self.is_mine and self.is_revealed : return "M"
        if not self.is_revealed : return "*"
        if self.is_revealed : return str(self.adj_mine_count)



















