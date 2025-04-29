# This is going to be trying things out with JUST TEXT in the terminal

import random

def grid():
    grid = [[0 for row in range(3)] for col in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = f"{i}{j} "
    print('\n'.join(map(''.join, grid))) # map() applies a function to each item in an iterable. .join combines all items into one string. In this case, each row is separated by a newline

def grid2():
    empty_cell = "n"
    grid = [[0 for row in range(3)] for col in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = f"{empty_cell} "
    print('\n'.join(map(''.join, grid)))

def grid3():
    tiles = ["W", "C", "G"]
    grid = [[0 for row in range(3)] for col in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = random.choice(tiles)
    print('\n'.join(map(' '.join, grid)))

def grid4():
    empty_cell = "n"
    tiles = ["W", "C", "G"]
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = empty_cell
    
    row = random.randint(0,2)
    col = random.randint(0,2)
    print(f"Coordinates: {row},{col}")
    grid[row][col] = random.choice(tiles)

    print('\n'.join(map(' '.join, grid)))

def grid5():
    empty_cell = "n"
    tiles = ["W", "C", "G"]
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = empty_cell
    
    row = random.randint(0,2)
    col = random.randint(0,2)
    print(f"Coordinates: {row},{col}")
    print(findNeighbors(row, col, 3, 3))
    grid[row][col] = random.choice(tiles)

    print('\n'.join(map(' '.join, grid)))

def findNeighbors(coord_row, coord_col, grid_row, grid_col):
    north = "none"
    if coord_row != 0:
        north = f"{coord_row - 1},{coord_col}"

    east = "none"
    if coord_col != grid_col:
        east = f"{coord_row},{coord_col + 1}"

    south = "none"
    if coord_row != grid_row:
        south = f"{coord_row + 1},{coord_col}"

    west = "none"
    if coord_col != 0:
        west = f"{coord_row},{coord_col - 1}"
    
    text = f"\nNeighbor locations:\n\nnorth = {north}\neast = {east}\nsouth = {south}\nwest = {west}\n"
    return text

def main():
    grid5()

if __name__ == "__main__":
    main()

