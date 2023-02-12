from copy import deepcopy
from sets import PieceSets
import numpy
import matplotlib.pyplot as plt

class Blockudoku:

    def __init__(self, board = None) -> None:
        if board == None:
            self.board = numpy.zeros((9, 9), int)
        else:
            self.board = numpy.ndarray(board)
        
        self.piece_set = PieceSets(type='normal')

    def print_board(self):
        print(self.board)

    def show_board(self):
        plt.matshow(self.board)
        plt.show()

    def placeable_in_position(self, piece, start_i, start_j):
        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    if start_i + i > len(self.board) - 1 or start_j + j > len(self.board[0]) - 1:
                        return False
                    if self.board[start_i + i][start_j + j] == 1:
                        return False
        return True

    def place(self, piece, start_i, start_j):
        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    self.board[start_i + i][start_j + j] = 1
        
    def check(self):
        rows = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cols = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for i in range(9):
            for j in range(9):
                rows[i] += self.board[i][j]
                cols[j] += self.board[i][j]
                squares[(i // 3) * 3 + j // 3] += self.board[i][j]

        # cancella le colonne, righe o quadrati completi

        for i in range(9):
            if rows[i] == 9:
                self.board[i][:] = 0
        for j in range(9):
            if cols[j] == 9:
                self.board[:][j] = 0
        if squares[0] == 9: self.board[0:3][0:3] = 0
        if squares[1] == 9: self.board[0:3][3:6] = 0
        if squares[2] == 9: self.board[0:3][6:9] = 0
        if squares[3] == 9: self.board[3:6][0:3] = 0
        if squares[4] == 9: self.board[3:6][3:6] = 0
        if squares[5] == 9: self.board[3:6][6:9] = 0
        if squares[6] == 9: self.board[6:9][0:3] = 0
        if squares[7] == 9: self.board[6:9][3:6] = 0
        if squares[8] == 9: self.board[6:9][6:9] = 0



if __name__ == "__main__":
    blockudoku = Blockudoku()
    pieces = blockudoku.piece_set.get_set()
    
    print('inizio')
    blockudoku.print_board()

    blockudoku.place(pieces[7], 7, 0)
    blockudoku.check()
    print('1 pezzo')
    blockudoku.print_board()

    blockudoku.place(pieces[12], 6, 1)
    blockudoku.check()
    print('2 pezzi')
    blockudoku.print_board()

    blockudoku.place(pieces[8], 6, 3)
    blockudoku.check()
    print('3 pezzi')
    blockudoku.print_board()

    blockudoku.place(pieces[8], 6, 6)
    blockudoku.check()
    print('4 pezzi')
    blockudoku.print_board()

    blockudoku.place(pieces[0], 6, 0)
    blockudoku.check()
    print('4 pezzi')
    blockudoku.print_board()
    

