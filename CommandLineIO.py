'''Defines a text driven IO for a given minesweeper board instance'''

END_ASCII_COLOR_SEQUENCE = '\033[0m'
ASCII_COLOR_SEQUENCE_MAP = {
    1 : '\033[94m', # Blue
    2 : '\033[32m', # Green
    3 : '\033[31m', # Red
    4 : '\033[34m', # Dark Blue
    5 : '\033[35m', # Magenta (usually Brown but it's not available)
    6 : '\033[36m', # Cyan
    7 : '\033[30m', # Black
    8 : '\033[90m'  # Gray
}

class CommandLineIO:

    def __init__(self, board):
        self.board = board
    
    # TODO: Need to add line numbers to the board printout
    def prettyPrintBoard(self):
        s = ""
        for row in self.board.tiles:
          for tile in row:
            if tile.flagged:
              s += "F "
            elif tile.hidden:
                s += '\033[37m' + "?" + END_ASCII_COLOR_SEQUENCE + " "
            elif tile.number == 0:
              s += "  "
            elif tile.isBomb:
              s += "* "
            else:
              s += ASCII_COLOR_SEQUENCE_MAP[tile.number] + str(tile.number) + END_ASCII_COLOR_SEQUENCE + " "
          s += "\n"
        print(s)
    
    def start(self):
        while not self.board.gameOver and not self.board.gameWin:
            self.prettyPrintBoard()
            userInput = raw_input()
            # TODO: Need to sanitize user input
            tokens = userInput.split(" ")
            command = tokens[0]
            x = int(tokens[1])
            y = int(tokens[2])

            if command == "left":
                self.board.leftClick(x, y)
            elif command == "right":
                self.board.rightClick(x, y)

        if self.board.gameOver:
            print("BOOM")
        if self.board.gameWin:
            print("WIN")