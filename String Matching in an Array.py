# My solution for this Problem....

class Solution:
    # Time Complexity: O(n^2 * k), where n is the number of words and k is the average length of the words.
    # Space Complexity: O(r)

    def stringMatching(self, words: List[str]) -> List[str]:
        # Sort words by length to ensure shorter words are compared against longer ones.
        words.sort(key=len)
        result = []

        # Iterate through each word using its index.
        for i in range(len(words)):
            # Compare the current word with all subsequent words.
            for j in range(i + 1, len(words)):
                # Check if the current word is a substring of the other word.
                if words[i] in words[j]:
                    result.append(words[i])
                    break  # Stop further comparisons for this word once added.

        return result
