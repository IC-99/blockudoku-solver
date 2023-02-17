from blockudoku_game import Blockudoku
from board import Board
import numpy

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

    def future_eval(self, board: Board, future = None):
        if future.__class__ == None.__class__:
            future = self.blockudoku.piece_set.get_set()

        future_eval = 0
        future_rate = 0.5
        for p in future:
            temp_board = Board(board.grid)
            future_eval += self.find_future_place(p, temp_board)[1] / len(future)

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
    
    
    def find_place(self, piece, board = None):
        if board.__class__ == None.__class__:
            board = self.blockudoku.board

        position = None
        max_eval = -numpy.inf
        
        for i in range(9):
            for j in range(9):
                if board.placeable_in_position(piece, i, j):
                    new_board = Board(board.grid)
                    new_board.place(piece, i, j)
                    new_new_board = Board(new_board.grid)
                    eval = self.eval(new_board) # + self.future_eval(new_new_board)
                    # print('valutazione attuale:', eval)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        # print('valutazione:', max_eval)
        return (position, max_eval)

    def find_and_place(self, piece):

        position = self.find_place(piece)[0]
        if position == None:
            return False
        i, j = position
        blockudoku.place(piece, i, j)
        return True

    def find_and_place_more_pieces_in_board(self, piece, rest, board: Board):
        position = None
        max_eval = -numpy.inf
        future = rest

        for i in range(9):
            for j in range(9):
                if board.placeable_in_position(piece, i, j):
                    new_board = Board(board.grid)
                    new_board.place(piece, i, j)
                    new_new_board = Board(new_board.grid)
                    eval = self.eval(new_board) + self.future_eval(new_new_board, future)
                    # print('valutazione attuale:', eval)
                    if eval > max_eval:
                        position = (i, j)
                        max_eval = eval

        # print('valutazione:', max_eval)
        return (position, max_eval)


    def eval_order(self, pieces):
        new_board = Board(blockudoku.board.grid)

        position1, eval1 = self.find_and_place_more_pieces_in_board(pieces[0], [pieces[1], pieces[2]], new_board)
        if position1 == None:
            return (None, -numpy.inf)
        new_board.place(pieces[0], position1[0], position1[1])
        new_board.update()

        position2, eval2 = self.find_and_place_more_pieces_in_board(pieces[1], [pieces[2]], new_board)
        if position2 == None:
            return (None, -numpy.inf)
        new_board.place(pieces[1], position2[0], position2[1])
        new_board.update()

        position3, eval3 = self.find_place(pieces[2], new_board)
        if position3 == None:
            return (None, -numpy.inf)
        new_board.place(pieces[2], position3[0], position3[1])
        new_board.update()
        
        return ([position1, position2, position3], eval1 + eval2 + eval3)
    
    def find_and_place_three(self, pieces):
        options = []
        options.append([pieces[0], pieces[1], pieces[2]])
        options.append([pieces[0], pieces[2], pieces[1]])
        options.append([pieces[1], pieces[0], pieces[2]])
        options.append([pieces[1], pieces[2], pieces[0]])
        options.append([pieces[2], pieces[0], pieces[1]])
        options.append([pieces[2], pieces[1], pieces[0]])

        max_eval = -10000
        best_option = None
        found_one = False
        best_positions = None

        for i in range(len(options)):
            # print('elaborando opzione', i)
            positions, eval = self.eval_order(options[i])
            # print('valutazione opzione', i, '=', eval)
            if positions != None:
                found_one = True
                if eval > max_eval:
                    best_option = i
                    max_eval = eval
                    best_positions = positions

        if found_one:
            print('')
            print('soluzione trovata:')
            for i in range(3): 
                print(options[best_option][i])
                print('in posizione:', best_positions[i])
                print('')
            blockudoku.place_three(options[best_option], best_positions)

        return found_one                

    def simulate(self):
        placed = 1
        print('inizio')

        while True:
            blockudoku.print()
            # blockudoku.show()
            print('mossa', placed, 'punti:', blockudoku.points)

            pieces_to_place = self.blockudoku.piece_set.get_three()
            print('posizionanado:')
            print('pezzo 1: ')
            print(pieces_to_place[0])
            print('pezzo 2: ')
            print(pieces_to_place[1])
            print('pezzo 3: ')
            print(pieces_to_place[2])

            if not self.find_and_place_three(pieces_to_place):
                break

            blockudoku.update()
            placed += 3

        print('partita terminata. piazzati', placed - 1, 'pezzi.', 'punteggio:', blockudoku.points)

    def solver(self):
        placed = 1
        print('inizio')

        while True:
            blockudoku.print()
            blockudoku.show()
            print('mossa', placed, 'punti:', blockudoku.points)

            # gestione input
            while True:
                pieces_to_place = []

                for i in range(3):
                    while True:
                        print('pezzo', i + 1)
                        index = int(input('inserisci ID pezzo:'))
                        if index > 0 and index <= len(blockudoku.piece_set.get_set()):
                            pieces_to_place.append(blockudoku.piece_set.get_set()[index - 1])
                            break
                        print('pezzo non disponibile')
                
                print('posizionanado:')
                print('pezzo 1: ')
                print(pieces_to_place[0])
                print('pezzo 2: ')
                print(pieces_to_place[1])
                print('pezzo 3: ')
                print(pieces_to_place[2])

                while True:
                    res = input('sono corretti? (y/n)\n')
                    if res == 'y' or res == 'n':
                        break
                    else:
                        print('risposta non valida')

                if res == 'y':
                    break

            print('elaborazione in corso')
            
            if not self.find_and_place_three(pieces_to_place):
                break

            blockudoku.update()
            placed += 3

        print('partita terminata. piazzati', placed - 1, 'pezzi.', 'punteggio:', blockudoku.points)

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

    lst = [[0, 0, 0, 1, 1, 1, 1, 1, 0], \
           [0, 0, 0, 0, 1, 0, 0, 1, 0], \
           [0, 0, 0, 0, 1, 0, 0, 0, 0], \
           [0, 1, 1, 0, 0, 0, 0, 0, 0], \
           [0, 1, 0, 0, 0, 0, 0, 0, 0], \
           [0, 1, 0, 0, 0, 0, 1, 1, 0], \
           [0, 1, 1, 1, 1, 1, 1, 1, 0], \
           [0, 0, 0, 1, 0, 0, 0, 0, 0], \
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(9):
        for j in range(9):
            grid[i][j] = lst[i][j]
    
    # grid = numpy.zeros((9, 9), int)
    board = Board(grid)
    blockudoku = Blockudoku(board, 'plus')
    solver = Solver(blockudoku)
    
    solver.simulate()
