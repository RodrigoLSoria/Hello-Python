import random 
import re


#lets create a board objcet to represent the minesweeper game
# this is so that we can just say "create a new board objcet" or
# "dig here", or "render this game for this subject"
class Board:
    def __init__(self, dim_size=10, num_bombs=10):
        # lets keep track of this parameters, they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
            # helper function!
        self.board = self.make_new_board() #plant the bombs 
        self.assign_values_to_board()


        # initialize a set to keep track of which locations we've uncovered 
        # we'll save (row, col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        # construct a new board base on the dim size and num of bombs
        # we should contruct the list of list here

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size 
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this means there's a bomb planted there already so keep going 
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # here we assign a number from 0 to 8 for all empty spaces, which represents 
        # who many neighbouring bombs there are. we can precomute these and it'll save effoty
        # checking what aroung the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # it this is a bomb we dont want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)

    def get_num_neighbouring_bombs(self, row, col):
        # let's iterate through each of the neighbouring positions and sum number of bombs 
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # lef: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom left: (row+1, col+1)

        # make sure not to go out of bounds!

        num_neighbouring_bombs = 0
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, dont check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        
        return num_neighbouring_bombs

    def dig(self, row, col):
         # dig at that location
         # return true if succesful dig, false if bomb dug

         self.dug.add((row,col)) # to keep track that we dug here

         if self.board[row][col] == '*':
             return False
         elif self.board[row][col] > 0:
             return True

         # self.board[row][col] = 0
         for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        
         return True

    def __str__(self):
        # if you call print on this object, it wil print out what this function returns
        # return a string that show the board to the player

        # first lets create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if(row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string 
        string_rep = ''

        #get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))

        indices_row += ' |'.join(cells) 
        indices_row += ' |\n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bomb show game over
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory!

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input('Where would you like to dig? input as row,col: ')) # '0, 3'
        row, col =int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print('invalid location, try again.')
            continue

        # if it's valid we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break
    # 2 ways to end loop, lets check which one
    if safe:
        print('Congratulations, you are victorious!')
    else:
        print('Sorry, game over')
        # let's reveal the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__=='__main__':
    play()
