# My solution for this Problem....

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        #Time Complexity: O(n + m), where `n` is the length of nums1 and `m` is the length of nums2.
        #Space Complexity: O(1), as no additional space is used beyond variables.
        l1 = len(nums1)  # Length of nums1.
        l2 = len(nums2)  # Length of nums2.

        xor = 0  # Initialize the XOR result.

        # If nums1 has an odd number of elements, each element of nums2 will appear in the result an odd number of times.
        if l1 % 2 != 0:
            for val in nums2:
                xor ^= val  # XOR all elements of nums2.

        # If nums2 has an odd number of elements, each element of nums1 will appear in the result an odd number of times.
        if l2 % 2 != 0:
            for val in nums1:
                xor ^= val  # XOR all elements of nums1.

        return xor  # Return the final XOR value.
