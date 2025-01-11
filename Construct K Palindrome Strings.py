# My solution for this Problem....

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #Time Complexity: O(n), where `n` is the length of the string `s`.
        #Space Complexity: O(c), where `c` is the number of unique characters in `s`.

        l = len(s)  # Length of the string `s`.

        # If there are fewer characters in `s` than `k`, it's impossible to construct `k` palindromes.
        if l < k:
            return False

        # If the number of characters equals `k`, each character can form its own palindrome.
        if l == k:
            return True

        # Count the frequency of each character in the string.
        dit = Counter(s)

        # Count the number of characters with odd frequencies.
        odd_freq = 0
        for key, val in dit.items():
            if val % 2 != 0:
                odd_freq += 1

        # It's possible to construct `k` palindromes if the number of odd-frequency characters is ≤ `k`.
        return odd_freq <= k
