def find

def solve_sudoku(puzzle):
    #it's going to  solve our sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku
    #mutates the puzzle to be the solution (if solution exists)

    #step 1: choose somewhere on the puzzle to make a guess 
    row, col = find_next_empty(puzzle)