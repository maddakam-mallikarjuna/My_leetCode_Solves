# My solution for this Problem....

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #Time Complexity: O(n + r * c), where `n` is the length of `arr`, `r` is the number of rows, and `c` is the number of columns in `mat`.
        #Space Complexity: O(r * c), due to the space used by `coord_dict` to store coordinates of the matrix elements.
        
        c = len(mat[0])
        r = len(mat)
        
        # Arrays to track the number of painted cells in each row and column
        painted_rows = [0] * r
        painted_cols = [0] * c
        
        # Dictionary to store the coordinates of each value in the matrix
        coord_dict = {}
        for i in range(r): 
            for j in range(c): 
                coord_dict[mat[i][j]] = (i, j)
        
        # Paint the matrix according to the values in `arr`
        for i, val in enumerate(arr):
            row, col = coord_dict[val]  # Get the coordinates of the value in the matrix
            
            # Increment the painted count for the corresponding row and column
            painted_rows[row] += 1
            painted_cols[col] += 1
            
            # Check if the current row or column is completely painted
            if painted_rows[row] == c or painted_cols[col] == r:
                return i  # Return the index where the first complete row or column is painted
