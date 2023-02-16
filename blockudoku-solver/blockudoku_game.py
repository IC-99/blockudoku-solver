from copy import deepcopy
from sets import PieceSet
from board import Board
import numpy
from numpy.random import randint
import matplotlib.pyplot as plt

class Blockudoku:

    def __init__(self, board: Board = None, piece_set: PieceSet = None) -> None:
        if board.__class__ == None.__class__:
            board = Board()
        self.board = board
        
        if piece_set.__class__ == None.__class__:
            piece_set = PieceSet()
        
        self.piece_set = piece_set

        self.points = 0
    
    def print(self):
        self.board.print_board()
    
    def show(self):
        self.board.show_board()

    def get_piece(self):
        return self.piece_set.get_one()

    def end(self, piece):
        return not self.board.placeable(piece)

    def placeable_in_position(self, piece, i, j):
        return self.board.placeable_in_position(piece, i, j)
    
    def place(self, piece, i, j):
        if self.placeable_in_position(piece, i, j):
            self.board.place(piece, i, j)
            return True
        return False

    def place_three(self, pieces, positions):
        for i in range(3):
            if self.placeable_in_position(pieces[i], positions[i][0], positions[i][1]):
                self.board.place(pieces[i], positions[i][0], positions[i][1])
                self.update()
            else:    
                print('posizione non valida')
                return False

    def update(self):
        self.points += self.board.check()

    def play(self):
        placed = 1
        print('inizio')

        while True:
            self.print()
            print('mossa', placed, 'punti:', self.points)

            piece = self.get_piece()
            print('posizionando: ')
            print(piece)

            if self.end(piece):
                break

            self.show()

            while True:
                i = int(input('inserisci riga:'))
                j = int(input('inserisci colonna:'))
                if self.place(piece, i, j):
                    break
                else:
                    print('posizione non valida')

            self.update()
            placed += 1

        print('partita terminata. piazzati', placed - 1, 'pezzi', 'punteggio:', self.points)

if __name__ == "__main__":
    grid = numpy.zeros((9, 9), int)

    lst = [[1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1, 1]]
    for i in range(9):
        for j in range(9):
            grid[i][j] = lst[i][j]

    blockudoku = Blockudoku(board=Board(grid))
    
    blockudoku.play()
