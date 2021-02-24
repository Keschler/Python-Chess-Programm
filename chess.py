import chess

uniDict = {"WHITE": {0: "♙", 1: "♖", 2: "♘", 3: "♗", 4: "♔", 5: "♕", 6: "."},
           "BLACK": {0: "♟", 1: "♜", 2: "♞", 3: "♝", 4: "♚", 5: "♛", 6: "."}}


class Game:
    def __init__(self):
        self.current_color = 0  # Which color is playing | 0 = WHITE 1 = BLACK
        self.chess_board = chess.Board()
        self.board = [[
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []] for i in range(8)]  # Nice looking board
        self.create_default_Board()
        self.show_current_board()
        self.start()

    def create_default_Board(self):
        """
        Create Default Board
        """
        for i in range(0, 8):
            if i == 0:  # If first line
                self.board[i][0] = uniDict["WHITE"][1]
                self.board[i][1] = uniDict["WHITE"][2]
                self.board[i][2] = uniDict["WHITE"][3]
                self.board[i][3] = uniDict["WHITE"][4]
                self.board[i][4] = uniDict["WHITE"][5]
                self.board[i][5] = uniDict["WHITE"][3]
                self.board[i][6] = uniDict["WHITE"][2]
                self.board[i][7] = uniDict["WHITE"][1]
            elif i == 7:
                self.board[i][0] = uniDict["BLACK"][1]
                self.board[i][1] = uniDict["BLACK"][2]
                self.board[i][2] = uniDict["BLACK"][3]
                self.board[i][3] = uniDict["BLACK"][4]
                self.board[i][4] = uniDict["BLACK"][5]
                self.board[i][5] = uniDict["BLACK"][3]
                self.board[i][6] = uniDict["BLACK"][2]
                self.board[i][7] = uniDict["BLACK"][1]
            else:
                for j in range(8):
                    if j % 2 == 0:  # Every Second time
                        self.board[i][j] = uniDict["WHITE"][6]
                    else:
                        self.board[i][j] = uniDict["BLACK"][6]

    def show_current_board(self):
        """
        Print current board
        """
        print("a | b | c | d | e | f | g | h")
        for i in range(8):
            print("   ".join(self.board[i]))

    def make_move(self):
        """
        Make current move
        """
        # Converts the number where the figure is
        current_field_choose = 0
        current_line_choose = 8 - int(self.user_input_choose[1])
        current_field_where = 0
        current_line_where = 8 - int(self.user_input_where[1])
        for j in range(8):
            # Convert current_field_choose
            if self.user_input_choose[0] == "a":
                current_field_choose = 0
            elif self.user_input_choose[0] == "b":
                current_field_choose = 1
            elif self.user_input_choose[0] == "c":
                current_field_choose = 2
            elif self.user_input_choose[0] == "d":
                current_field_choose = 3
            elif self.user_input_choose[0] == "e":
                current_field_choose = 4
            elif self.user_input_choose[0] == "f":
                current_field_choose = 5
            elif self.user_input_choose[0] == "g":
                current_field_choose = 6
            elif self.user_input_choose[0] == "h":
                current_field_choose = 7
            # Convert current_field_where
            if self.user_input_where[0] == "a":
                current_field_where = 0
            elif self.user_input_where[0] == "b":
                current_field_where = 1
            elif self.user_input_where[0] == "c":
                current_field_where = 2
            elif self.user_input_where[0] == "d":
                current_field_where = 3
            elif self.user_input_where[0] == "e":
                current_field_where = 4
            elif self.user_input_where[0] == "f":
                current_field_where = 5
            elif self.user_input_where[0] == "g":
                current_field_where = 6
            elif self.user_input_where[0] == "h":
                current_field_where = 7
        print(current_line_where, current_field_where)
        figure_choose = self.board[current_line_choose][current_field_choose]
        figure_where = self.board[current_line_where][current_field_where]
        print("Line", self.board[current_line_choose][current_field_choose])
        self.board[current_line_where][current_field_where] = self.board[current_line_choose][
                current_field_choose]  # Move selected figure
        self.board[current_line_choose][current_field_choose] = "."  # Insert a blank field at the selected figure

    def start(self):
        while True:
            try:
                if self.current_color == 0:
                    print("White is playing")
                else:
                    print("Black is playing")

                self.user_input_choose = str(input("which figure do you want to choose? zB(g1)"))
                self.user_input_where = str(input("Where should it go? zB(h3)"))
            except ValueError:
                print("Give me a right value!")
            move = chess.Move.from_uci(self.user_input_choose + self.user_input_where)  # Convert it
            if move in self.chess_board.legal_moves:  # If move is legal
                self.chess_board.push(move)  # Make move in chess library
                self.make_move()
                self.current_color = 1 - self.current_color  # Switch color
                self.show_current_board()
            else:
                print("Please give right values!")


if __name__ == '__main__':
    game = Game()  # Start game
