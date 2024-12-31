# My solution for this Problem....

class Solution:
    # Time Complexity: O(n * k)      # Space Complexity: O(1)
    def findWords(self, words: List[str]) -> List[str]:
        # Define rows of the keyboard
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        # Initialize a list to store the result
        res = []

        # Iterate over each word in the list
        for word in words:
            # Get the first character of the word (lowercased)
            ele = word[0].lower()
            row = row1  # Default to row1
            
            # Determine which row the first character belongs to
            if ele in row2:
                row = row2
            elif ele in row3:
                row = row3
            
            # Check if all characters in the word belong to the same row
            if all(i in row for i in word.lower()):
                # Add the word to the result list if condition is satisfied
                res.append(word)
        
        # Return the list of valid words
        return res
