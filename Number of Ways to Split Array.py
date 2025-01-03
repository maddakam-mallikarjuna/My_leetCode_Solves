# My solution for this Problem....

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Time Complexity: O(n), where n is the length of nums.
        # Space Complexity: O(1), as we are using constant space.

        n = len(nums)
        total = sum(nums)

        count = 0
        prefix = 0
        
        # Iterate through the array, excluding the last element.
        for i in range(n - 1):
            prefix += nums[i]  # Update the prefix sum.
            
            # Check if the prefix sum is greater than or equal to the remaining sum.
            if total - prefix <= prefix:
                count += 1  # Increment the count of valid splits.
            
        return count  # Return the total number of valid splits.
