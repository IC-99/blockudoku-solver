from copy import deepcopy
from blockudoku_game import Blockudoku
from board import Board
import numpy
from numpy.random import randint
import matplotlib.pyplot as plt

class Solver:

    def __init__(self, blockudoku: Blockudoku) -> None:
        self.blockudoku = blockudoku

    def eval(self, board: Board):
        
        eval = 0
        bonus = 300
        bonus_free = 20
        bonus_border = 5
        malus_single = 30
        bonus_near_row = 10
        bonus_near_cols = 10
        bonus_near_squares = 20
        malus_islands = 50
        malus_lakes = 50
        bonus_square = 20
        
        # valutazione colonne, righe o quadrati completi:
        eval = bonus * board.update()

        # valutazione spazi liberi
        pieces = self.blockudoku.piece_set.get_set()

        for p in pieces[18:]:
            if board.placeable(p):
                eval += bonus_free

        # valutazione bordi
        eval += (board.rows[0] + board.rows[-1] + board.cols[0] + board.cols[-1]) * bonus_border

        # valutazione spazi da 1
        eval -= board.count_single() * malus_single

        # valutazione combinazioni quasi raggiunte
        for r in board.rows:
            if r > 5:
                eval += bonus_near_row
        for c in board.cols:
            if c > 5:
                eval += bonus_near_cols
        for s in board.squares:
            if s > 5:
                eval += bonus_near_squares
            if s == 0:
                eval += bonus_square

        # valutazione arcipelaghi

        temp_board = Board(board.grid)
        eval -= temp_board.islands() * malus_islands

        # valutazione laghi
        temp_board = Board(board.grid)
        eval -= temp_board.lakes() * malus_lakes

        return eval

    def future_eval(self, board: Board):

        pieces = self.blockudoku.piece_set.get_set()
        future_eval = 0
        future_rate = 0.5
        for p in pieces:
            temp_board = Board(board.grid)
            future_eval += self.find_future_place(p, temp_board)[1] / len(pieces)

        return future_eval * future_rate

    def find_future_place(self, piece, board: Board):

        position = None
        max_eval = -2000
        
        for i in range(9):
            for j in range(9):
                if self.blockudoku.placeable_in_position(piece, i, j):
                    new_board = Board(board.grid)
                    new_board.place(piece, i, j)
                    eval = self.eval(new_board)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        return (position, max_eval)
    
    
    def find_place(self, piece):

        position = None
        max_eval = -numpy.inf
        
        for i in range(9):
            for j in range(9):
                if self.blockudoku.placeable_in_position(piece, i, j):
                    new_board = Board(self.blockudoku.board.grid)
                    new_board.place(piece, i, j)
                    new_new_board = Board(new_board.grid)
                    eval = self.eval(new_board) + self.future_eval(new_new_board)
                    # print('valutazione attuale:', eval)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        print('valutazione:', max_eval)
        return (position, max_eval)

    def find_and_place(self, piece):

        position = self.find_place(piece)[0]
        if position == None:
            return False
        i, j = position
        blockudoku.place(piece, i, j)
        return True

    def simulate(self):
        placed = 1
        points = 0
        print('inizio')

        while True:
            blockudoku.print()
            print('mossa', placed, 'punti:', points)

            piece = self.blockudoku.piece_set.get_one()
            print('posizionando: ')
            print(piece)

            if not self.find_and_place(piece):
                break

            # self.show_board()

            points += blockudoku.update()
            placed += 1

        print('partita terminata. piazzati', placed - 1, 'pezzi.', 'punteggio:', points)

if __name__ == "__main__":
    grid = numpy.zeros((9, 9), int)
    
    lst = [[1, 0, 0, 1, 1, 0, 0, 0, 0], \
           [1, 0, 0, 1, 1, 1, 1, 0, 0], \
           [1, 1, 1, 1, 1, 1, 1, 0, 0], \
           [1, 0, 0, 0, 0, 0, 1, 0, 0], \
           [1, 0, 0, 0, 1, 0, 0, 0, 0], \
           [0, 0, 1, 0, 1, 0, 1, 0, 0], \
           [0, 0, 1, 1, 1, 1, 1, 0, 1], \
           [0, 0, 0, 1, 1, 0, 0, 0, 1], \
           [0, 0, 0, 0, 1, 1, 1, 1, 1]]

    for i in range(9):
        for j in range(9):
            grid[i][j] = lst[i][j]
    
    #grid = numpy.zeros((9, 9), int)
    board = Board(grid)
    blockudoku = Blockudoku(board)
    solver = Solver(blockudoku)
    
    solver.simulate()
