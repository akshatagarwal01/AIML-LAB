def check_position(grid, r, c):
    for i in range(r):
        if grid[i][c] == 'Q':
            return False

    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if grid[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    (i, j) = (r, c)
    while i >= 0 and j < len(grid):
        if grid[i][j] == 'Q':
            return False 
        i = i - 1
        j = j + 1
 
    return True
 
 
def printSolution(grid):
    for r in grid:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
 
 
def nQueen(grid, r):
 
    
    if r == len(grid):
        printSolution(grid)
        return
 
    for i in range(len(grid)):
 
 
        if check_position(grid, r, i):
            grid[r][i] = 'Q'
            nQueen(grid, r + 1)
            grid[r][i] = '–'
 
 

N = 8
grid = [['–' for x in range(N)] for y in range(N)]

nQueen(grid, 0)