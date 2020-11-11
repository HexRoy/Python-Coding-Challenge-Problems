# Problem:
# You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board.
# The only pieces on the board are the black king and various white pieces.
# Given this matrix, determine whether the king is in check.
# For details on how each piece moves, see here.
# For example, given the following matrix:

# ...K....
# ........
# .B......
# ......P.
# .......R
# ..N.....
# ........
# .....Q..
# You should return True, since the bishop is attacking the king diagonally.

#=====================================================================================================================

# Solution:
#   We assume there can only be one king on the 'board' because there is no way to differentiate between white and
#       black king
#   We assume the bottom of the 'board' is where we started for the sake of pawn movement
#   We assume pawns will not make it/ or begin in the top row to be converted into another piece

class Chess:
    def __init__(self, board):
        """
        :param board: the given 8x8 matrix representing the chess board
        """
        self.board = board
        self.king_x = None
        self.king_y = None
        self.check = False
        self.pieces = []
        self.search_for_piece()

    def search_for_piece(self):
        """
        search: finds and adds all pieces to the list
        :return: N/A
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'K':
                    self.king_x = j
                    self.king_y = i
                elif self.board[i][j] != '.':
                    self.pieces.append([self.board[i][j], i, j])
        self.check_for_check()

    def check_for_check(self):
        """
        check_for_check: Searches through found pieces to see if king is in check
        :return: True if king is in check/ Else False
        """
        for piece in self.pieces:
            if piece[0] == 'Q':
                # Queen uses rook + bishops checks
                self.bishops([piece[1], piece[2]])
                self.rook([piece[1], piece[2]])
            if piece[0] == 'R':
                self.rook([piece[1], piece[2]])
            if piece[0] == 'B':
                self.bishops([piece[1], piece[2]])
            if piece[0] == 'N':
                self.knight([piece[1], piece[2]])
            if piece[0] == 'P':
                self.pawn([piece[1], piece[2]])

        if self.check:
            print("You are in check")
        else:
            print("You are not in check")

    def rook(self, pos):
        """
        rook: Checks all cardinal directions around the rook for king
        :param pos: list of two ints containing the position of the rook
        :return: N/A
        """
        # If they are in the same row, checks left or right
        if pos[0] == self.king_y:
            if pos[1] > self.king_x:
                for i in range(pos[1] - 1, self.king_x, -1):
                    if self.board[pos[0]][i] != ".":
                        return
                self.check = True
                return
            if pos[1] < self.king_x:
                for i in range(pos[1] + 1, self.king_x):
                    if self.board[pos[0]][i] != ".":
                        return
                self.check = True
                return

        # If they are in the same column, checks up or down
        if pos[1] == self.king_x:
            if pos[0] > self.king_y:
                for i in range(pos[0] - 1, self.king_y, -1):
                    if self.board[i][pos[1]] != ".":
                        return
                self.check = True
                return
            if pos[0] < self.king_y:
                for i in range(pos[0] + 1, self.king_y):
                    if self.board[i][pos[1]] != ".":
                        return
                self.check = True
                return

    def bishops(self, pos):
        """
        bishops: checks all diagonals around piece for king
        :param pos: list of two ints containing the position of the bishops
        :return: N/A
        """
        # If on same height cannot attack
        if pos[0] == self.king_y:
            return
        # If on same row cannot attack
        if pos[1] == self.king_x:
            return

        # If bishop above king
        if pos[0] < self.king_y:
            # If bishop to the top left of king
            if pos[1] < self.king_x:
                while True:
                    pos[0] += 1
                    pos[1] += 1

                    # You are in check
                    if self.board[pos[0]][pos[1]] == "K":
                        self.check = True
                        return

                    # Hit another piece
                    if self.board[pos[0]][pos[1]] != ".":
                        return

                    # Hit edge
                    if pos[0] == 7:
                        return
                    if pos[1] == 7:
                        return

            # Else bishop on the top right of king
            else:
                while True:
                    pos[0] += 1
                    pos[1] -= 1

                    # You are in check
                    if self.board[pos[0]][pos[1]] == "K":
                        self.check = True
                        return

                    # Hit another piece
                    if self.board[pos[0]][pos[1]] != ".":
                        return

                    # Hit edge
                    if pos[0] == 8:
                        return
                    if pos[1] == 0:
                        return

        # Else bishop below king
        else:
            # If bishop to the bottom left of king
            if pos[1] < self.king_x:
                while True:
                    pos[0] -= 1
                    pos[1] += 1

                    # You are in check
                    if self.board[pos[0]][pos[1]] == "K":
                        self.check = True
                        return

                    # Hit another piece
                    if self.board[pos[0]][pos[1]] != ".":
                        return

                    # Hit edge
                    if pos[0] == 0:
                        return
                    if pos[1] == 7:
                        return

            # Else bishop on the bottom right of king
            else:
                while True:
                    pos[0] -= 1
                    pos[1] -= 1

                    # You are in check
                    if self.board[pos[0]][pos[1]] == "K":
                        self.check = True
                        return

                    # Hit another piece
                    if self.board[pos[0]][pos[1]] != ".":
                        return

                    # Hit edge
                    if pos[0] == 0:
                        return
                    if pos[1] == 0:
                        return

    def knight(self, pos):
        """
        knight: makes sure the bounds are valid then checks every spot for king
        :param pos: list of two ints containing the position of the knight
        :return: N/A
        """
        if pos[1] <= 6:
            if self.board[pos[0] - 2][pos[1] + 1] == "K":
                self.check = True
        if pos[1] <= 5:
            if self.board[pos[0] - 1][pos[1] + 2] == "K":
                self.check = True
        if pos[0] <= 5 and pos[1] <= 6:
            if self.board[pos[0] + 2][pos[1] + 1] == "K":
                self.check = True
        if pos[0] <= 6 and pos[1] <= 5:
            if self.board[pos[0] + 1][pos[1] + 2] == "K":
                self.check = True
        if pos[0] <= 6:
            if self.board[pos[0] + 1][pos[1] - 2] == "K":
                self.check = True
        if pos[0] <= 5:
            if self.board[pos[0] + 2][pos[1] - 1] == "K":
                self.check = True
        if self.board[pos[0] - 1][pos[1] - 2] == "K":
            self.check = True
        if self.board[pos[0] - 2][pos[1] - 1] == "K":
            self.check = True

    def pawn(self, pos):
        """
        pawn: checks one space diagonally upward for king
        :param pos: list of two ints containing the position of the pawn
        :return: N/A
        """
        # If pawn is in the top row
        if pos[0] == 0:
            return
        else:
            if self.king_y == pos[0]-1:
                if self.king_x == pos[1] + 1 or self.king_x == pos[1] - 1:
                    self.check = True
                    return
            return



Chess([
    ['.', '.', '.', 'K', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'P', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'R'],
    ['.', '.', 'N', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '', '.', '.', '.', 'Q', '.', '.'],
])
