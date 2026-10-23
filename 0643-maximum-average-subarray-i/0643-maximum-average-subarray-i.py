class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cursum=sum(nums[:k])
        maxsum=sum(nums[:k])
        for i in range(k,len(nums)):
            cursum+=nums[i]-nums[i-k]
            maxsum=max(cursum,maxsum)
        return maxsum/k    

        