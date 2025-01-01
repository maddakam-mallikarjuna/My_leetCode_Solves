# My solution for this Problem....

class Solution:
    # Function to calculate the maximum score by splitting the string.
    # Time Complexity: O(n)      # Space Complexity: O(1)
    def maxScore(self, s: str) -> int:
        max_score = 0  # Variable to track the maximum score
        count_zeros_left = 0  # Count of zeros in the left partition
        count_ones_right = s.count("1")  # Count of ones in the right partition initially

        # Iterate through the string, excluding the last index to ensure valid splits
        for i in range(len(s) - 1):
            # Update the count of zeros in the left partition
            count_zeros_left += s[i] == "0"
            # Update the count of ones in the right partition
            count_ones_right -= s[i] == "1"
            # Calculate the score for the current split and update the maximum score
            max_score = max(max_score, count_zeros_left + count_ones_right)

        # Return the maximum score found
        return max_score
