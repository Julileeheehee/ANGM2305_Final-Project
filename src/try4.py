import random

TILES = ["W", "C", "G"]

TILERULES = {
    'W': ["W", "W", "W", "W"],
    'C': ["C", "C", "C", "C"],
    'G': ["G", "G", "G", "G"]
}

NORTH = 0
EAST = 1
WEST = 2
SOUTH = 3

class Cell():
    def __init__(self):
        self.possibilities = TILES # Should start out with 3 in this case
        self.entropy = len(self.possibilities)
    
    def getEntropy(self):
        return str(self.entropy)


def main_grid():
    empty_cell = "n"
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = empty_cell

    print('\n'.join(map(' '.join, grid)))

def entropy_grid():
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = Cell().getEntropy()

    print('\n'.join(map(' '.join, grid)))


def main():
    print("\nMain Grid:")
    main_grid()
    print("------------------")
    print("Entropy Grid:")
    entropy_grid()

if __name__ == "__main__":
    main()