# My solution for this Problem....

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        #Time Complexity: O(log(n)), where `n` is the value of `start XOR goal`.
        #Space Complexity: O(1).

        # XOR of start and goal gives the bits that differ between them
        differing_bits = start ^ goal
        flip_count = 0

        # Count the number of set bits (1s) in differing_bits
        while differing_bits > 0:
            # Increment flip_count for each bit that is set
            flip_count += differing_bits & 1
            # Right shift differing_bits to check the next bit
            differing_bits >>= 1

        return flip_count
