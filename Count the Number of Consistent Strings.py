# My solution for this Problem....

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        #Time Complexity: O(n * m), where `n` is the number of words and `m` is the average word length.
        #Space Complexity: O(k), where `k` is the number of unique characters in `allowed`.

        # Convert `allowed` string to a set for O(1) membership checks
        allowed_chars = set(allowed)
        consistent_count = 0

        # Iterate through each word in the `words` list
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(character in allowed_chars for character in word):
                consistent_count += 1  # Increment count if the word is consistent

        return consistent_count
