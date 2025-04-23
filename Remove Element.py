# My solution for this Problem....
class Solution:
    # Time Complexity: O(n)      # Space Complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index to track the position of non-val elements
        for i in range(len(nums)):
            if nums[i] != val:  # If the current element is not equal to `val`
                nums[k] = nums[i]  # Move it to the front of the array
                k += 1
        return k  # Return the new length of the array

#Method - 2
class Solution:
    # Time Complexity: O(n^2)    # Space Complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        # Get the initial length of the array
        l = len(nums)

        # Initialize index pointer
        i = 0

        # Iterate through the array
        while i < l:
            if nums[i] == val:  # If the current element is equal to `val`
                nums.remove(val)  # Remove the element
                l -= 1  # Decrease the length of the array
            else:
                i += 1  # Move to the next index
