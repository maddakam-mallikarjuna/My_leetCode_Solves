# My solution for this Problem....

def isPrefixAndSuffix(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    
    # If str1 is longer than str2, it can't be a prefix or suffix.
    if l1 > l2:
        return False

    # Check if str1 matches the prefix and suffix of str2.
    if str1 == str2[:l1] and str1 == str2[-l1:]:
        return True

    return False

class Solution:
    # Time Complexity: O(n^2 * k), where n is the number of words, and k is the average word length.
    # Space Complexity: O(1) - no additional space apart from variables.
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Count pairs of words where one word is both a prefix and suffix of another.
        """
        l = len(words)
        count = 0
        
        # Nested loops to check each pair of words.
        for i in range(l):
            for j in range(i + 1, l):
                # Increment count if words[i] is both a prefix and suffix of words[j].
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count
