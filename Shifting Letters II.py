# My solution for this Problem....

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Time Complexity: O(n + shifts)
        # Space Complexity: O(n)

        l = len(s)

        # Initialize an array to track the net effect of shifts.
        app = [0] * (l + 1)

        # Process each shift in the `shifts` list.
        for st, end, d in shifts:
            # Increment at the start index and decrement at the position after end.
            app[st] += (d * 2 - 1)  # +1 for clockwise, -1 for counterclockwise.
            app[end + 1] -= (d * 2 - 1)

        # Compute the prefix sum of `app` to determine the effective shifts for each character.
        app = list(accumulate(app))

        res = ""  # Resultant shifted string.

        # Iterate through the string and apply shifts to each character.
        for i, count in enumerate(s):
            # Calculate the new character after applying shifts.
            t = (app[i] + ord(count) - 97) % 26 + 97
            if t < 97: 
                t += 26  # Ensure character remains within lowercase alphabet range.
            res += chr(t)  # Append the shifted character to the result.

        return res
