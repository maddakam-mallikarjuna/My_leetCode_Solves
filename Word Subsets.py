# My solution for this Problem....

from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #Time Complexity: O(n * m), where `n` is the length of `words1` and `m` is the average length of words in `words1`.
        #Space Complexity: O(k), where `k` is the total number of unique characters in `words2`.
        
        result = []  # List to store the result.
        tempDict = Counter()  # Counter to store the max frequency of each character in `words2`.

        # Build a counter for the characters in all words of `words2` (taking the max frequency).
        for w in words2:
            tempDict |= Counter(w)

        # Check each word in `words1` to see if it contains all required characters.
        for w in words1:
            # If the current word has all characters from `words2`, add it to the result.
            if not tempDict - Counter(w):
                result.append(w)

        return result
