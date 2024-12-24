# My solution for this Problem....

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      window = 0  # Maximum consecutive ones
      count = 0   # Current count of consecutive ones

      for num in nums:
          if num == 1:
              count += 1  # Increment count for consecutive ones
              window = max(window, count)  # Update the maximum window
          else:
              count = 0  # Reset count if a 0 is encountered

      return window

#Method - 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
				# Time Complexity: O(n)		# Space Complexity: O(1)
        count = 0
        max_ones = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                max_ones = max(max_ones, count)
                count = 0

        return max(max_ones, count)

  
