# My solution for this Problem....

class Solution:
    # Time Complexity: O(n), where n is the length of the string `boxes`. Each pass over the string (prefix, postfix, and final calculation) takes O(n).
    # Space Complexity: O(n), due to the `prefix`, `postfix`, and `res` lists.

    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)

        # Prefix array to calculate the operations moving from left to right.
        prefix = [0] * l
        increment = 0  # Tracks the number of '1's seen so far.
        for i in range(l):
            if boxes[i] == '1':  # If the current box contains a ball.
                increment += 1  # Increment the ball count.
            prefix[i] += increment  # Add the count to the prefix.
            if i + 1 < l:  # Propagate the cumulative count to the next index.
                prefix[i + 1] += prefix[i]

        # Postfix array to calculate the operations moving from right to left.
        postfix = [0] * l
        increment = 0  # Reset increment for the right-to-left pass.
        for i in range(l - 1, -1, -1):
            if boxes[i] == '1':  # If the current box contains a ball.
                increment += 1  # Increment the ball count.
            postfix[i] += increment  # Add the count to the postfix.
            if i - 1 >= 0:  # Propagate the cumulative count to the previous index.
                postfix[i - 1] += postfix[i]

        # Adjust the prefix and postfix arrays to compute final results.
        prefix = [0] + prefix[:-1]  # Shift prefix to align with valid indices.
        postfix = postfix[1:] + [0]  # Shift postfix similarly.

        # Compute the result by summing prefix and postfix at each index.
        res = []
        for i in range(l):
            res.append(prefix[i] + postfix[i])

        return res
