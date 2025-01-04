# My solution for this Problem....

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        res = []  # List to store the indices that meet the condition.
        count = 0  # Counter to track the index of the current element in `variables`.

        for i in variables:
            # Calculate the value of ((i[0] ** i[1]) % 10) ** i[2].
            temp = ((i[0] ** i[1]) % 10) ** i[2]
            
            if temp % i[-1] == target:
                res.append(count)
            
            count += 1
        
        return res
