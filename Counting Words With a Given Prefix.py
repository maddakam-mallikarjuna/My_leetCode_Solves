# My solution for this Problem....

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #Time Complexity: O(n * m), where `n` is the number of words, and `m` is the length of the prefix.
        #Space Complexity: O(1), as no extra space is used other than a counter.
        
        count = 0  # Initialize the count of matching words.

        for word in words:
            if word.startswith(pref):  # Check if the word starts with the given prefix.
                count += 1  # Increment the count if true.

        return count

        """
        Method - 2
        count = 0

        for word in words:
            # Compare the prefix of the word with the given `pref`.
            if word[:len(pref)] == pref:
                count += 1

        return count
        """
