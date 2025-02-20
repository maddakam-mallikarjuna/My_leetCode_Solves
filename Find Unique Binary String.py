#My solution........

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums)
        n = len(nums[0])

        nums_have = set()
        nums_to = set(range(2 ** n))

        for i in nums:
            nums_have.add(int(i, 2))
        
        for i in nums_to:
            if i not in nums_have:
                x = str(bin(i))
                return x[2:].zfill(n)
