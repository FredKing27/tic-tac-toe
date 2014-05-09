class Board:
    def __init__(self):
        # initializes a 3x3 tic-tac-toe board, which looks like
        self.board = [[' ' for i in xrange(3)] for j in xrange(3)]

    # board.add_tile('X', (1, 1))
    # the location is stored as a tuple
    # for more on tuples, visit: http://www.tutorialspoint.com/python/python_tuples.htm
    def add_tile(self, tile, location):
        self.board[location[0]][location[1]] = tile

    # prints board to console
    def printBoard(self):
        for row in self.board:
            line = " | "
            for slot in row:
                line += slot + ' | '
            print line
            print "---------------"

class Player:
    # player = Player('X', 1)
    def __init__(self, tile, number):
        self.tile = tile
        self.number = number

class Game:
    def __init__(self):
        self.board = Board()
        self.play()

    # play a game until it has been won
    def play(self):
        self.start()
        turn = 0
        self.board.printBoard()
        while not self.isWon():
            if turn is 0: # player 0's turn
                self.move(self.playerZero)
            else: # player 1's turn
                self.move(self.playerOne)
            self.board.printBoard()
            turn = (turn + 1) % 2 # will alternate between 0 and 1. Why is this?
    
    # have player make a move
    def move(self, player):
        print "Player {0}, what is your move?".format(player.number)
        move = self._getMove()
        while not self.board.board[move[0]][move[1]] == ' ':
            print "Invalid Move. Please try again"
            move = self._getMove()
        self.board.board[move[0]][move[1]] = player.tile
    
    # get move coordinates from player
    # the underscore indicates that this is an internal method
    # , which means that it should only be called by another method of this class
    def _getMove(self):
        row = raw_input("Row: (0 - 2) ")[0]
        while not row.isdigit() or (int(row) < 0 or int(row) > 2):
            row = raw_input("Invalid Input. Row: (0 - 2) \n")[0]
        col = raw_input("Column: (0 - 2) ")[0]
        while not col.isdigit() or (int(col) < 0 or int(col) > 2) :
            col = raw_input("Invalid Input. Column: (0 - 2) \n")[0]
        row, col = int(row), int(col) # convert from string to int
        return (row, col)
    
    # start a new game
    # mostly just getting player tile choices
    def start(self):
        print "Player 0, what tile would you like to play (X or O)?"
        playerZeroTile = raw_input()[0].upper()
        while not playerZeroTile == 'X' and not playerZeroTile == 'O':
            playerZeroTile = raw_input("Invalid input. Player 0, what tile would you like to play (X or O)? \n")[0].upper()
        self.playerZero = Player(playerZeroTile, 0)
        if playerZeroTile == 'X':
            self.playerOne = Player('O', 1)
        else:
            self.playerOne = Player('X', 1)
        print "Player 1, your tile is {0}".format(self.playerOne.tile)       
        
    def isWon(self):
        pass

def main():
    print "Welcome to Tic-Tac-Toe"
    newGame = "Y"
    while newGame is "Y":
        game = Game()
        newGame = raw_input("Start a new game? (Y/N) \n").upper()
        if not newGame is "Y" and not newGame is "N":
            newGame = raw_input("Invalid input. Start a new game? (Y/N)").upper()

if __name__ == "__main__":
    main()


