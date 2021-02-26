import chess
from string import ascii_lowercase

uniDict = {"WHITE": {0: "♟", 1: "♖", 2: "♘", 3: "♗", 4: "♕", 5: "♔", 6: "."},
           "BLACK": {0: "♙", 1: "♜", 2: "♞", 3: "♝", 4: "♛", 5: "♚", 6: "."}}


class Game:
    def __init__(self):
        self.current_color = "WHITE"
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
        self.create_default_board()
        self.show_current_board()
        self.start()

    def create_default_board(self):
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
            elif i == 1:
                for s in range(8):  # Create pawns
                    self.board[1][s] = uniDict["BLACK"][0]  # For black
                    self.board[6][s] = uniDict["WHITE"][0]  # For white
            elif i == 7:  # If last line
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
                    if self.board[i][j] != uniDict["WHITE"][0]:  # If the field is empty
                        self.board[i][j] = uniDict["WHITE"][6]

    def show_current_board(self):
        """
        Print current board
        """
        for i in range(8):
            line = abs(-8 + i)
            print("   ".join(self.board[i]), line)
        print("a | b | c | d | e | f | g | h")

    def make_move(self):
        """
        Make current move
        """
        # Converts the number where the figure is
        current_field_choose = 0
        current_line_choose = 8 - int(self.user_input_choose[1])
        current_field_where = 0
        current_line_where = 8 - int(self.user_input_where[1])

        current_field_choose = ascii_lowercase.index(self.user_input_choose[0])  # Convert chess language
        current_field_where = ascii_lowercase.index(self.user_input_where[0])  # Convert chess language

        self.board[current_line_where][current_field_where] = self.board[current_line_choose][
            current_field_choose]  # Move selected figure
        # Insert a blank field at the selected figure
        self.board[current_line_choose][current_field_choose] = "."

    def switch_color(self):
        if self.current_color == "WHITE":
            return "BLACK"
        else:
            return "WHITE"

    def start(self):
        while True:
            print(self.current_color, ": is playing!")
            self.user_input_choose = str(
                input("which figure do you want to choose? zB(g1)"))
            self.user_input_where = str(
                input("Where should it go? zB(h3)"))
            # If input is not 2
            if len(self.user_input_where) != 2 or (len(self.user_input_choose) != 2):
                print("Give a right value!")
                continue
            move = chess.Move.from_uci(
                self.user_input_choose + self.user_input_where)  # Convert it
            if move in self.chess_board.legal_moves:  # If move is legal
                self.chess_board.push(move)  # Make move in chess library
                self.make_move()
                self.current_color = self.switch_color()
                self.show_current_board()
                if self.chess_board.is_game_over():
                    print(self.current_color, "won!")
                    self.chess_board.reset()
                    if input("Do you wanna play again y/n").lower() == "y":
                        Game()
                    else:
                        break
            else:
                print("Please give right values!")


if __name__ == '__main__':
    game = Game()  # Start game
