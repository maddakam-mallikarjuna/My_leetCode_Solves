# My solution for this Problem.....

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time Complexity: O(numRows ^ 2)	# Space Complexity: O(numRows ^ 2)
        # Initialize the result with the first row of Pascal's triangle.
        finalNums = [[1]]
        
        # Build each subsequent row based on the previous row.
        for i in range(1, numRows):
            # Start the new row with 1.
            newRow = [1]
            
            # Compute the inner elements by summing adjacent elements in the previous row.
            for j in range(len(finalNums[i - 1]) - 1):
                newRow.append(finalNums[i - 1][j] + finalNums[i - 1][j + 1])
            
            # End the row with 1 and add it to the result.
            newRow.append(1)
            finalNums.append(newRow)
        
        return finalNums
