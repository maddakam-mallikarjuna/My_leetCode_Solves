# My solution for this Problem....

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        #Time Complexity: O(n^2), where `n` is the length of the arrays `A` and `B`.
        #Space Complexity: O(n), as the `freq` dictionary stores the frequency of up to `n` unique elements.
                                                                                
        l = len(A)  # Length of the input arrays.
        result = []  # List to store the resulting prefix common array.
        freq = {}  # Dictionary to store the frequency of elements from A and B.

        for i in range(l):
            # Update the frequency of the current element in A.
            if A[i] in freq:
                freq[A[i]] += 1
            else:
                freq[A[i]] = 1

            # Update the frequency of the current element in B.
            if B[i] in freq:
                freq[B[i]] += 1
            else:
                freq[B[i]] = 1

            # Calculate the count of common elements in the current prefix.
            result.append(sum(1 for _, j in freq.items() if j >= 2))

        return result
