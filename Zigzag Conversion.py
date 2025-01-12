# My solution for this Problem....

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #Time Complexity: O(n), where `n` is the length of the string `s`.
        #Space Complexity: O(n), for storing the characters in the rows.
        
        # If only one row or the number of rows exceeds the string length, return the original string.
        if numRows == 1 or numRows >= len(s):
            return s

        # `idx` keeps track of the current row, and `d` determines the direction (1 for down, -1 for up).
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]  # Initialize a list of lists to store characters for each row.

        # Iterate through each character in the string.
        for char in s:
            rows[idx].append(char)  # Add the character to the current row.

            # Change direction at the first or last row.
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1

            # Move to the next row based on the direction.
            idx += d

        # Combine characters in each row to form strings.
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        # Concatenate all rows to get the final result.
        return ''.join(rows)
