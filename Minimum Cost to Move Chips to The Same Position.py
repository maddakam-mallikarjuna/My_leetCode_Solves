# My solution for this Problem....

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Initialize counters for chips at even and odd positions
        # Time Complexity: O(n)      # Space Complexity: O(1)
        evenCount = 0
        oddCount = 0

        # Count the number of chips at even and odd positions
        for pos in position:
            if pos % 2:  # If position is odd
                oddCount += 1
            else:  # If position is even
                evenCount += 1
              
        return min(oddCount, evenCount)
