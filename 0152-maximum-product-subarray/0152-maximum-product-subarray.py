class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res=nums[0]
        curmin=nums[0]
        curmax=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                curmax,curmin=curmin,curmax
            curmax=max(n,curmax*n)
            curmin=min(n,curmin*n)
            res=max(res,curmax)
        return res        

        