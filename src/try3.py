# This is going to be trying things out with JUST TEXT in the terminal

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

def main():
    grid2()

if __name__ == "__main__":
    main()

