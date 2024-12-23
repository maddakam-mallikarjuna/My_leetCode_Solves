# My solution with Baisc loops and iteration through each ele
# Time Complexity: O(243) ≈ O(1) (constant due to fixed board size).
# Space Complexity: O(81) ≈ O(1) (constant space due to fixed board size).

def valid_row(board, n):
    # Check if a specific row 'n' contains duplicate numbers.
    row = board[n]
    seen = set()  # Keep track of seen numbers.
    
    for i in row:
        if i == ".":  # Ignore empty cells.
            pass
        elif i not in seen:  # Add number to the set if not seen before.
            seen.add(i)
        else:  # Duplicate found.
            return False
    return True

def valid_col(board, n):
    # Check if a specific column 'n' contains duplicate numbers.
    col = list(zip(*board))[n]  # Extract the column by transposing the matrix.
    seen = set()  # Keep track of seen numbers.
    
    for i in col:
        if i == ".":  # Ignore empty cells.
            pass
        elif i not in seen:  # Add number to the set if not seen before.
            seen.add(i)
        else:  # Duplicate found.
            return False
    return True

def valid_grids(board):
    # Check if 3x3 subgrids contain duplicate numbers.
    res = []
    
    # Iterate over every cell in the board.
    for i in range(9):
        for j in range(9):
            ele = board[i][j]
            if ele != ".":  # For non-empty cells, map to its subgrid and keep track of its value.
                res.append((i // 3, j // 3, ele))  # Identify subgrid by (row // 3, col // 3).

    # If duplicates exist in subgrids, the lengths of `res` and `set(res)` will differ.
    return len(res) == len(set(res))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate all rows and columns.
        for i in range(9):
            if not valid_row(board, i) or not valid_col(board, i):
                return False

        # Validate all 3x3 subgrids.
        if not valid_grids(board):
            return False

        # Return True if all checks pass.
        return True

# Onether's solution with less code
"""
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
			"""
