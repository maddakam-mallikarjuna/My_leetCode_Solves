# My solution for this Problem.....

def bitCount(num):
    #Time Complexity: O(log(num)), where `log(num)` is the number of bits in `num`.
    #Space Complexity: O(1), as no additional space is used.

    count = 0
    while num > 0:
        if num & 1:  # Check if the least significant bit is 1.
            count += 1
        num >>= 1  # Right shift `num` by 1 bit.
    return count

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #Time Complexity: O(log(num1) + |a - b|), where `log(num1)` is the number of bits in `num1` and `|a - b|` is the difference in the number of set bits.
        #Space Complexity: O(1), as no additional space is used.
        
        # Count the number of set bits (1s) in num1 and num2.
        a = bitCount(num1)
        b = bitCount(num2)

        # If the number of set bits matches, return num1.
        if a == b:
            return num1

        # Initialize the result as num1.
        res = num1

        if b < a:
            # Reduce the number of set bits in `res` to match `b`.
            for _ in range(a - b):
                res = res & (res - 1)  # Turn off the least significant set bit.
        else:
            # Increase the number of set bits in `res` to match `b`.
            for _ in range(b - a):
                res = res | (res + 1)  # Turn on the next least significant unset bit.

        return res
