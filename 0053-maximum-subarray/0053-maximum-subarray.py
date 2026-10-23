class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ms=float('-inf')
        cs=0
        for x in nums:
            cs+=x
            if cs>ms:
                ms=cs
            if cs<0:
                cs=0
        return ms        


        