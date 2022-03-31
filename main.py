import math
import itertools

class board_class:
    def __init__(self, board):
        self.board = board
        self.board_3x3 = []
        board_cache = []
        board_cache_2 = []
        for i in range(3):
            for j in range(3):
                board_cache.append(self.board[i * 3][j * 3:(j + 1) * 3])
                board_cache.append(self.board[(i * 3) + 1][j * 3:(j + 1) * 3])
                board_cache.append(self.board[(i * 3) + 2][j * 3:(j + 1) * 3])
                self.board_3x3.append(board_cache)
                board_cache = []

    def find_column(self, x):
        result = []
        for i in self.board:
            result.append(i[x])
        return result

    def find_row(self, y):
        return self.board[y]

    def find_box(self, x, y):
        x_cache = math.ceil((x+1)/3)-1
        y_cache = math.ceil((y+1)/3)-1
        posibilities_y = []
        posibilities = []
        for i in range(3):
            posibilities.append(i * 3 + x_cache)
        posibilities_y = list(range(y_cache*3, y_cache*3+3))
        element = list(set(posibilities_y).intersection(posibilities))
        return list(itertools.chain(*self.board_3x3[element[0]]))


    def check(self):
        for n, i in enumerate(self.board):
            for m, j in enumerate(i):
                if j == 0:
                    neighbours = self.find_box(m, n)+self.find_row(n)+ self.find_column(m)
                    neighbours = list(set(neighbours))
                    posibilites = list(range(1, 10))
                    if 0 in neighbours:
                        neighbours.pop(neighbours.index((0)))
                    for i in neighbours:
                        posibilites.pop(posibilites.index(i))
                    if len(posibilites) == 1:
                        self.board[n][m] = posibilites[0]

        self.board_3x3 = []
        board_cache = []
        for i in range(3):
            for j in range(3):
                board_cache.append(self.board[i * 3][j * 3:(j + 1) * 3])
                board_cache.append(self.board[(i * 3) + 1][j * 3:(j + 1) * 3])
                board_cache.append(self.board[(i * 3) + 2][j * 3:(j + 1) * 3])
                self.board_3x3.append(board_cache)
                board_cache = []

    def get_board(self):
        return self.board
#give the board as a 2d list
board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]
run_class = board_class(board)
run = True
x = 0
while run:
    run_class.check()
    if 0 not in list(itertools.chain(*run_class.get_board())):
        run = False
    x += 1
    print(x)
for i in run_class.get_board():
    print(i)
