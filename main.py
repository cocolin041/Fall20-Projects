import random

class Puzzle:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.hint_v = [[]]
        self.hint_h = [[]]
        self.grid = [[]]

    def generate_puzzle(self, width: int, height: int):
        self.height = height
        self.width = width
        self.grid = [[''] * self.width for _ in range(self.height)]

        for row in range(self.height):
            filled_cells_idx = random.sample(range(0, self.width), random.randint(1, self.width))
            for idx in filled_cells_idx:
                self.grid[row][idx] = 'B'

        self.generate_hint()

    def generate_hint(self):
        self.hint_h = [[] for _ in range(self.width)]
        self.hint_v = [[] for _ in range(self.height)]

        for col in range(self.width):
            black_count = 0
            for row in range(self.height):
                if self.grid[row][col] == 'B':
                    black_count += 1
                    if (row+1 < self.height and self.grid[row+1][col] == '') or row+1 == self.height:
                        self.hint_h[col].append(black_count)
                        black_count = 0

        for row in range(self.height):
            blank_count = 0
            for col in range(self.width):
                if self.grid[row][col] == '':
                    blank_count += 1
                    if (col+1 < self.width and self.grid[row][col+1] == 'B') or col+1 == self.width:
                        self.hint_v[row].append(blank_count)
                        blank_count = 0

    def print_puzzle(self):

        for i in range(len(max(self.hint_h, key=lambda l: len(l)))):
            for x in self.hint_h:
                if i < len(x):
                    print(' '+str(x[i]), end='')
                else:
                    print('', end='')
            print('')

        for row in range(self.height):
            for col in range(self.width):
                if col == 0:
                    print('|⎺|', end='')
                else:
                    print('⎺|', end='')
            for x in self.hint_v[row]:
                print(x, end=' ')

            print('')


if __name__ == '__main__':
    height = int(input('Enter the height:'))
    width = int(input('Enter the height:'))

    p = Puzzle()
    p.generate_puzzle(height, width)
    p.print_puzzle()
