# My solution for this Problem....

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time Complexity: O(n), where `n` is the length of the strings `s` and `t`.
        #Space Complexity: O(u), where `u` is the number of unique characters in `s`.
      
        # If lengths of the strings are not the same, they cannot be anagrams.
        if len(s) != len(t):
            return False
        
        # Create a set of unique characters from the first string.
        unique_chars = set(s)

        # Check if the frequency of each character in `s` matches that in `t`.
        for char in unique_chars:
            if s.count(char) != t.count(char):
                return False
        
        # If all checks pass, the strings are anagrams.
        return True

# Method - 2
return Counter(s) == Counter(t)
