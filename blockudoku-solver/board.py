from copy import deepcopy
from sets import PieceSet
import numpy
from numpy.random import randint
import matplotlib.pyplot as plt

class Board:

    def __init__(self, grid = None) -> None:
        if grid.__class__ == None.__class__:
            grid = numpy.zeros((9, 9), int)
        self.grid = deepcopy(grid)

        self.rows =     [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cols =     [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.squares =  [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def print_board(self):
        print(self.grid)
    
    def show_board(self):
        plt.matshow(self.grid)
        plt.show()
    
    def placeable_in_position(self, piece, start_i, start_j):
        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    if start_i + i > 8 or start_j + j > 8:
                        return False
                    if self.grid[start_i + i][start_j + j] == 1:
                        return False
        return True

    def placeable(self, piece):
        for start_i in range(9):
            for start_j in range(9):
                if self.placeable_in_position(piece, start_i, start_j):
                    return True
        return False

    def place(self, piece, start_i, start_j):
        for i in range(piece.shape[0]):
            for j in range(piece.shape[1]):
                if piece[i][j] == 1:
                    self.grid[start_i + i][start_j + j] = 1
        
    def update_stats(self):
        self.rows =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cols =    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(9):
            for j in range(9):
                self.rows[i] += self.grid[i][j]
                self.cols[j] += self.grid[i][j]
                self.squares[(i // 3) * 3 + j // 3] += self.grid[i][j]
    
    def update(self):
        self.update_stats()

        cleared = 0
        
        # cancella le colonne, righe o quadrati completi:
        for i in range(9):
            if self.rows[i] == 9:
                self.grid[i, :] = 0
                cleared += 1
        for j in range(9):
            if self.cols[j] == 9:
                self.grid[:, j] = 0
                cleared += 1
        if self.squares[0] == 9: 
            self.grid[0:3, 0:3] = 0
            cleared += 1
        if self.squares[1] == 9: 
            self.grid[0:3, 3:6] = 0
            cleared += 1
        if self.squares[2] == 9: 
            self.grid[0:3, 6:9] = 0
            cleared += 1
        if self.squares[3] == 9: 
            self.grid[3:6, 0:3] = 0
            cleared += 1
        if self.squares[4] == 9: 
            self.grid[3:6, 3:6] = 0
            cleared += 1
        if self.squares[5] == 9: 
            self.grid[3:6, 6:9] = 0
            cleared += 1
        if self.squares[6] == 9: 
            self.grid[6:9, 0:3] = 0
            cleared += 1
        if self.squares[7] == 9: 
            self.grid[6:9, 3:6] = 0
            cleared += 1
        if self.squares[8] == 9: 
            self.grid[6:9, 6:9] = 0
            cleared += 1

        return cleared

    def check(self):
        bonus = 90
        points = self.update() * bonus
        return points
    
    def count_single(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    north = i - 1
                    east = j + 1
                    south = i + 1
                    west = j - 1

                    single = True
                    if north >= 0:
                        if self.grid[north, j] == 0:
                            single = False
                    if south < 9:
                        if self.grid[south, j] == 0:
                            single = False
                    if west >= 0:
                        if self.grid[i, west] == 0:
                            single == False
                    if east < 9:
                        if self.grid[i, east] == 0:
                            single = False

                    if single:
                        count += 1
        return count

    def islands(self):
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= 9 or j >= 9 or grid[i][j] != 1:
                return 
            grid[i][j] = 0
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        if sum(sum(self.grid)) == 0:
            return 0
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 1:
                    dfs(self.grid, i, j)
                    count += 1
        return count

    def lakes(self):        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= 9 or j >= 9 or grid[i][j] != 0:
                return 
            grid[i][j] = 1
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        if sum(sum(self.grid)) == 81:
            return 0
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    dfs(self.grid, i, j)
                    count += 1
                    
        return count