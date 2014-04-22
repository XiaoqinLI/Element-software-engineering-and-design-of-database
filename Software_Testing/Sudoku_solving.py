# CHALLENGE: 
#
# Use check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]


import copy
import sys

def sanity_check(G):
    digit_tuple = (0,1,2,3,4,5,6,7,8,9)
    if len(G) != 9:
        return None
    else:
        for entry in G:
            if len(entry) != 9:
                return None
            for digit in entry:
                if digit not in digit_tuple:
                    return None
    return True

def digit_check(L):
    counter = 0
    for entry in L:
        if entry == 0:
            counter += 1
    cache = set()
    for entry in L:
        cache.add(entry)
    if (len(cache) < 9 - counter ):
        return False
    else:
        return True

def row_check(G):
    for entry in G:
        temp = []
        for digit in entry:
            temp.append(digit)
        if digit_check(temp) == False:
            return False
    return True

def col_check(G):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(G[j][i])
        if digit_check(temp) == False:
            return False
    return True
        
def subgrid_check(G):
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp = []
            for k in range(i,i+3):
                for m in range(j,j+3):
                    temp.append(G[k][m])
            if digit_check(temp) == False:
                return False
    return True

def check_sudoku(grid):
    if sanity_check(grid):
        if row_check(grid):
            if col_check(grid):
                if subgrid_check(grid):
                    return True
                else:
                    return False             
            else:
                return False
        else:
            return False
    else:
        return None

def solve_sudoku (__grid):
    res = check_sudoku(__grid)
    if res is None or res is False:
        return res

    grid = copy.deepcopy(__grid)

    # find the first 0 element and change it to each of 1-9
    # recursively calling this function on the result.
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for n in range(1,10):
                    grid[row][col] = n
                    new = solve_sudoku(grid)
                    if new is not False:
                        return new

                return False
    return grid

print(solve_sudoku(easy))

