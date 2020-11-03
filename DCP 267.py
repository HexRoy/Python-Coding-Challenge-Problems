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


# Solution:
#   We assume there can only be one king on the board because there is no way to differentiate between white and
#       black king

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
                self.queen([piece[1], piece[2]])
            if piece[0] == 'R':
                self.rook([piece[1], piece[2]])
            if piece[0] == 'B':
                self.bishops([piece[1], piece[2]])
            if piece[0] == 'N':
                self.knight([piece[1], piece[2]])
            if piece[0] == 'P':
                self.pawn([piece[1], piece[2]])

        if self.check == True:
            print("You are in check")
        else:
            print("You are not in check")

    def queen(self, pos):
        """
        queen: check all cardinal directions as well as diagonals looking for king
        :return: True if king is in check/ Else False
        """
        # If they are in the same row, checks left or right
        if pos[0] == self.king_y:
            if pos[1] > self.king_x:
                for i in range(pos[1]-1, self.king_x, -1):
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

        # If they are in the same diagonal, checks diagonal




        # first check if king is in sight
        # check for other pieces blocking
        # possible elimiate some directions by testing where king is


    def rook(self, pos):
        pass

    def bishops(self,pos):
        pass

    def knight(self, pos):
        pass

    def pawn(self, pos):
        pass


Chess([
    ['.', '.', '.', 'K', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'P', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'R'],
    ['.', '.', 'N', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'Q', '.', '.'],
])
