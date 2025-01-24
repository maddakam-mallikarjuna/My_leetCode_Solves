# My solution for this Problem....

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        #Time Complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns in the grid.
        #Space Complexity: O(m + n), for storing row and column server counts.

        rows = len(grid)
        cols = len(grid[0])
        
        # Arrays to store the count of servers in each row and column.
        server_count_in_rows = [0] * rows
        server_count_in_cols = [0] * cols
        
        # Count the number of servers in each row and column.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    server_count_in_rows[row] += 1
                    server_count_in_cols[col] += 1
        
        # Count servers that can communicate with at least one other server.
        communicating_servers = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if server_count_in_rows[row] > 1 or server_count_in_cols[col] > 1:
                        communicating_servers += 1
        
        return communicating_servers
