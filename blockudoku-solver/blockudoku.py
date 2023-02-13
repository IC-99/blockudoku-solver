from copy import deepcopy
from sets import PieceSets
import numpy
from numpy.random import randint
import matplotlib.pyplot as plt

class Blockudoku:

    def __init__(self, board = None) -> None:
        if board.__class__ == None.__class__:
            board = numpy.zeros((9, 9), int)
        self.board = board
        self.piece_set = PieceSets(type='normal')
    
    def print_board(self):
        print(self.board)
    
    def show_board(self):
        plt.matshow(self.board)
        plt.show()
    
    def placeable_in_position(self, piece, start_i, start_j, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    if start_i + i > 8 or start_j + j > 8:
                        return False
                    if board[start_i + i][start_j + j] == 1:
                        return False
        return True

    def placeable(self, piece, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        res = True

        for start_i in range(9):
            for start_j in range(9):
                if self.placeable_in_position(piece, start_i, start_j, board):
                    return True
        
        return False

    def place(self, piece, start_i, start_j, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    board[start_i + i][start_j + j] = 1
        
        return board
        
    def check(self, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        rows =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cols =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        points = 0
        bonus = 90
        
        for i in range(9):
            for j in range(9):
                rows[i] += board[i][j]
                cols[j] += board[i][j]
                squares[(i // 3) * 3 + j // 3] += board[i][j]
        
        # cancella le colonne, righe o quadrati completi:

        for i in range(9):
            if rows[i] == 9:
                board[i, :] = 0
                points += bonus
        for j in range(9):
            if cols[j] == 9:
                board[:, j] = 0
                points += bonus
        if squares[0] == 9: 
            board[0:3, 0:3] = 0
            points += bonus
        if squares[1] == 9: 
            board[0:3, 3:6] = 0
            points += bonus
        if squares[2] == 9: 
            board[0:3, 6:9] = 0
            points += bonus
        if squares[3] == 9: 
            board[3:6, 0:3] = 0
            points += bonus
        if squares[4] == 9: 
            board[3:6, 3:6] = 0
            points += bonus
        if squares[5] == 9: 
            board[3:6, 6:9] = 0
            points += bonus
        if squares[6] == 9: 
            board[6:9, 0:3] = 0
            points += bonus
        if squares[7] == 9: 
            board[6:9, 3:6] = 0
            points += bonus
        if squares[8] == 9: 
            board[6:9, 6:9] = 0
            points += bonus

        return points
    
    def islands(self, board):
        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= 9 or j >= 9 or board[i][j] != 1:
                return 
            board[i][j] = 0
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)
        count = 0
        if sum(sum(board)) == 0:
            return 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == 1:
                    dfs(board, i, j)
                    count += 1
                    
        return count

    def lakes(self, board):
        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= 9 or j >= 9 or board[i][j] != 0:
                return 
            board[i][j] = 1
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)
        count = 0
        if sum(sum(board)) == 81:
            return 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    dfs(board, i, j)
                    count += 1
                    
        return count

    def eval(self, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        rows =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        cols =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        
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
        future_rate = 0.5
        
        for i in range(9):
            for j in range(9):
                rows[i] += board[i][j]
                cols[j] += board[i][j]
                squares[(i // 3) * 3 + j // 3] += board[i][j]
        
        # valutazione colonne, righe o quadrati completi:

        for i in range(9):
            if rows[i] == 9:
                board[i, :] = 0
                eval += bonus
        for j in range(9):
            if cols[j] == 9:
                board[:, j] = 0
                eval += bonus
        if squares[0] == 9: 
            board[0:3, 0:3] = 0
            eval += bonus
        if squares[1] == 9: 
            board[0:3, 3:6] = 0
            eval += bonus
        if squares[2] == 9: 
            board[0:3, 6:9] = 0
            eval += bonus
        if squares[3] == 9: 
            board[3:6, 0:3] = 0
            eval += bonus
        if squares[4] == 9: 
            board[3:6, 3:6] = 0
            eval += bonus
        if squares[5] == 9: 
            board[3:6, 6:9] = 0
            eval += bonus
        if squares[6] == 9: 
            board[6:9, 0:3] = 0
            eval += bonus
        if squares[7] == 9: 
            board[6:9, 3:6] = 0
            eval += bonus
        if squares[8] == 9: 
            board[6:9, 6:9] = 0
            eval += bonus

        # valutazione spazi liberi
        pieces = self.piece_set.get_set()

        for p in pieces[18:]:
            if self.placeable(p, board):
                eval += bonus_free

        # valutazione bordi
        eval += (rows[0] + rows[-1] + cols[0] + cols[-1]) * bonus_border

        # valutazione spazi da 1
        for i in range(9):
            for j in range(9):
                if board[i, j] == 0:
                    north = i - 1
                    east = j + 1
                    south = i + 1
                    west = j - 1

                    single = True
                    if north >= 0:
                        if board[north, j] == 0:
                            single = False
                    if south < 9:
                        if board[south, j] == 0:
                            single = False
                    if west >= 0:
                        if board[i, west] == 0:
                            single == False
                    if east < 9:
                        if board[i, east] == 0:
                            single = False

                    if single:
                        eval -= malus_single

        # valutazione combinazioni quasi raggiunte
        for r in rows:
            if r > 5:
                eval += bonus_near_row
        for c in cols:
            if c > 5:
                eval += bonus_near_cols
        for s in squares:
            if s > 5:
                eval += bonus_near_squares
            if s == 0:
                eval += bonus_square

        # valutazione arcipelaghi

        eval -= self.islands(deepcopy(board)) * malus_islands

        # valutazione laghi

        eval -= self.lakes(deepcopy(board)) * malus_lakes

        return eval

    def future_eval(self, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        pieces = self.piece_set.get_set()
        future_eval = 0
        future_rate = 0.5
        for p in pieces:
            future_eval += self.find_future_place(p, deepcopy(board))[1] / len(pieces)

        return future_eval * future_rate

    def find_future_place(self, piece, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        position = None
        max_eval = -2000
        
        for i in range(9):
            for j in range(9):
                if self.placeable_in_position(piece, i, j, board):
                    new_board = deepcopy(board)
                    self.place(piece, i, j, new_board)
                    eval = self.eval(new_board)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        return (position, max_eval)
    
    
    def find_place(self, piece, board = None):
        if board.__class__ == None.__class__:
            board = self.board

        position = None
        max_eval = -numpy.inf
        
        for i in range(9):
            for j in range(9):
                if self.placeable_in_position(piece, i, j, board):
                    new_board = deepcopy(board)
                    self.place(piece, i, j, new_board)
                    eval = self.eval(deepcopy(new_board)) + self.future_eval(deepcopy(new_board))
                    #print('valutazione attuale:', eval)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        print('valutazione:', max_eval)
        return (position, max_eval)

    def find_and_place(self, piece, board = None):
        if board.__class__ == None.__class__:
            board = self.board
        
        position = self.find_place(piece, board)[0]
        if position == None:
            return False
        start_i, start_j = position
        self.place(piece, start_i, start_j, board)
        return True

    def simulate(self):
        placed = 0
        while True:
            print('mossa', placed)
            p = self.piece_set.get_set()[randint(0, 38)]
            print('posizionando: ')
            print(p)
            #self.show_board()
            if not self.find_and_place(p):
                break
            self.check()
            self.print_board()
            placed += 1
        print('piazzati', placed, 'pezzi')

if __name__ == "__main__":
    grid = numpy.zeros((9, 9), int)
    lst = [[1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1, 1]]
    for i in range(9):
        for j in range(9):
            grid[i][j] = lst[i][j]
    grid = numpy.zeros((9, 9), int)
    blockudoku = Blockudoku(grid)
    pieces = blockudoku.piece_set.get_set()
    
    print('inizio')
    blockudoku.simulate()
