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

def grid6():
    empty_cell = "n"
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = empty_cell
    
    #row = random.randint(0,2)
    #col = random.randint(0,2)
    row = 1
    col = 1
    print(f"Coordinates: {row},{col}")
    neighbors = findNeighbors(row, col, 3, 3)
    randomNeighbor = assignRandomNeighbor(neighbors)
    

    firstTile = random.choice(tiles)
    nextTile = assignRandomTile(firstTile)

    grid[row][col] = firstTile

    grid[randomNeighbor[0]][randomNeighbor[1]] = nextTile

    if any('n' in sublist for sublist in grid):
        print("Still not collapsed")

    print('\n'.join(map(' '.join, grid)))

tilerules = {
    'W': ["W", "C"],
    'C': ["W", "C", "G"],
    'G': ["C", "G"]
}

tiles = ["W", "C", "G"]

def grid7():
    
    empty_cell = "n"
    grid = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = empty_cell
    row = random.randint(0,2)
    col = random.randint(0,2)
    #row = 1
    #col = 1

    curr_row = row
    curr_col = col

    firstTile = random.choice(tiles)
    currTile = firstTile

    #while any('n' in sublist for sublist in grid):
    grid[curr_row][curr_col] = currTile

    neighbors = findNeighbors(curr_row, curr_col, 3, 3)
    randomNeighbor = assignRandomNeighbor(neighbors, grid)
    nextTile = assignRandomTile(currTile)
    grid[randomNeighbor[0]][randomNeighbor[1]] = nextTile

    #handles 2nd iteration
    curr_row = randomNeighbor[0]
    curr_col = randomNeighbor[1]
    currTile = nextTile
    neighbors = findNeighbors(curr_row, curr_col, 3, 3)
    randomNeighbor = assignRandomNeighbor(neighbors, grid)
    nextTile = assignRandomTile(currTile)
    grid[randomNeighbor[0]][randomNeighbor[1]] = nextTile

    curr_row = randomNeighbor[0]
    curr_col = randomNeighbor[1]
    currTile = nextTile
    neighbors = findNeighbors(curr_row, curr_col, 3, 3)
    randomNeighbor = assignRandomNeighbor(neighbors, grid)
    nextTile = assignRandomTile(currTile)
    grid[randomNeighbor[0]][randomNeighbor[1]] = nextTile

        

    print('\n'.join(map(' '.join, grid)))

def findNeighbors(coord_row, coord_col, grid_row, grid_col):
    north = None
    if coord_row != 0:
        north = [coord_row - 1,coord_col]

    east = None
    if coord_col != grid_col - 1:
        east = [coord_row, coord_col + 1]

    south = None
    if coord_row != grid_row - 1:
        south = [coord_row + 1,coord_col]

    west = None
    if coord_col != 0:
        west = [coord_row,coord_col - 1]
    
    listofNeighbors = [north,east,south,west]
    return listofNeighbors

def assignRandomNeighbor(listofNeighbors, grid):
    #north = listofNeighbors[0]
    #east = listofNeighbors[1]
    #south = listofNeighbors[2]
    #west = listofNeighbors[3]
    copy_grid = grid
    print(copy_grid)
    choice = []
    for item in listofNeighbors:
        if item != None:
            i = item[0]
            j = item[1]
            if copy_grid[i][j] == 'n':
                choice.append(item)
    #print(choice)
    randomNeighbor = random.choice(choice)
    #print(randomNeighbor)
    return randomNeighbor

def assignRandomTile(firstTile):
    rules = tilerules[firstTile]
    randomTile = random.choice(rules)
    return randomTile



def main():
    grid7()

if __name__ == "__main__":
    main()

