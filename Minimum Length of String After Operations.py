# My solution for this Problem....

class Solution:
    def minimumLength(self, s: str) -> int:
        3Time Complexity: O(26 * n), where `n` is the length of the string `s`.
        #Space Complexity: O(1), as we use a fixed-size dictionary for the 26 alphabet characters.
        # Create a frequency map for all characters in the string.
          
        mp = {x: s.count(x) for x in "abcdefghijklmnopqrstuvwxyz"}
        count = 0

        # Iterate through the frequency map and calculate the contribution of each character.
        for i, j in mp.items():
            if j > 0:
                count += 2 - (j % 2)  # Add 2 for even frequencies, 1 for odd.

        return count
