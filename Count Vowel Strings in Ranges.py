# My solution for this Problem....

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Time Complexity: O(n + q), where n is the length of `words` and q is the number of queries.
        # Space Complexity: O(n), where n is the size of the prefix array.
        
        vows = ("a", "e", "i", "o", "u")
        l = len(words)

        # Initialize a prefix sum array of size `l + 1`
        prefix = [0] * (l + 1)

        # Build the prefix sum array
        for i in range(l):
            ele = words[i]
            prefix[i + 1] = prefix[i]  # Carry forward the previous prefix sum
            # Check if the current word starts and ends with a vowel
            if ele[0] in vows and ele[-1] in vows:
                prefix[i + 1] = prefix[i] + 1  # Increment prefix sum if true

        res = []

        # Process each query
        for i, j in queries:
            # Compute the count of vowel strings in the range [i, j]
            res.append(prefix[j + 1] - prefix[i])

        return res
