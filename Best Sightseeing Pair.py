# My solution for this Problem....
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Time Complexity: O(n)      # Space Complexity: O(1)

        maxVal = 0  # Maximum sightseeing score found so far
        cur = 0  # Maximum value of (values[j] + j) for previously visited indices

        for i in range(1, len(values)):  # Start from the second element
            # Update `cur` to maintain the best score of (values[j] + j) seen so far
            cur = max(cur, values[i - 1] + i - 1)

            # Calculate the score for the current pair (j, i) and update `maxVal`
            maxVal = max(maxVal, cur + values[i] - i)

        return maxVal
