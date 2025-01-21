# My solution for this Problem....

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        #Time Complexity: O(n), where `n` is the number of columns in the grid.
        #Space Complexity: O(1), as no extra space is used beyond a few variables.

        # Initialize the total sums for both rows.
        top_row_sum = sum(grid[0])
        bottom_row_sum = 0
        min_points_for_player2 = float('inf')  # Minimum points player 2 can guarantee.

        # Iterate through each column, calculating the remaining sums.
        for top_cell, bottom_cell in zip(grid[0], grid[1]):
            # Subtract the current cell value from the top row's remaining sum.
            top_row_sum -= top_cell
            
            # Calculate the worst-case points player 1 can leave.
            max_points_left = max(top_row_sum, bottom_row_sum)
            min_points_for_player2 = min(min_points_for_player2, max_points_left)
            
            # Add the current cell value to the bottom row's collected sum.
            bottom_row_sum += bottom_cell

        return min_points_for_player2
