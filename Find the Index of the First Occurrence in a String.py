# My solution for this Problem....

class Solution:
    # Time Complexity: O((l - n + 1) * n)      # Space Complexity: O(n) 
    def strStr(self, haystack: str, needle: str) -> int:
        # Length of the haystack
        l = len(haystack)
        # Length of the needle
        n = len(needle)

        # Loop through haystack from 0 to (l - n), inclusive
        for i in range(0, l - n + 1):
            # Extract the substring of length `n` starting from index `i`
            prefix = haystack[i : i + n]
            # Check if the substring matches the needle
            if prefix == needle:
                return i  # Return the starting index of the match
        
        # If no match is found, return -1
        return -1

#Other Solution
#Method- 1
class Solution:
    # Time Complexity: O(l * n)
    # Space Complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the built-in `find` function to locate the substring.
        # `find` returns the index of the first occurrence of `needle` in `haystack`, or -1 if not found.
        return haystack.find(needle)

