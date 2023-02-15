from copy import deepcopy
from sets import PieceSets
from board import Board
import numpy
from numpy.random import randint
import matplotlib.pyplot as plt

class Blockudoku:

    def __init__(self, board = None, piece_set = None) -> None:
        if board.__class__ == None.__class__:
            board = Board()
        self.board = board
        
        if piece_set.__class__ == None.__class__:
            piece_set = PieceSets()
        
        self.piece_set = piece_set
    
    def print(self):
        self.board.print_board()
    
    def show(self):
        self.board.show_board()

    def simulate(self):
        placed = 0
        self.board.print_board()

        while True:
            print('mossa', placed)

            p = self.piece_set.get_one()
            print('posizionando: ')
            print(p)

            #self.show_board()

            if not self.board.placeable(p):
                break

            while True:
                i = int(input('inserisci riga:'))
                j = int(input('inserisci colonna:'))
                if self.board.placeable_in_position(p, i, j):
                    self.board.place(p, i, j)
                    break
                else:
                    print('posizione non valida')

            self.board.check()
            self.board.print_board()
            placed += 1
        print('partita terminata. piazzati', placed, 'pezzi')

if __name__ == "__main__":
    grid = numpy.zeros((9, 9), int)

    lst = [[1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1, 1]]
    for i in range(9):
        for j in range(9):
            grid[i][j] = lst[i][j]

    blockudoku = Blockudoku(board=Board(grid))
    
    print('inizio')
    blockudoku.simulate()
