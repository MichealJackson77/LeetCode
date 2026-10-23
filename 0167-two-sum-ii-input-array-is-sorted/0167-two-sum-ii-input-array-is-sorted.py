class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
     # nums=list(map(int,input().split()))
      i=0
      j=len(nums)-1
      while i<j:

       tot=nums[i]+nums[j]
       if tot==target:
        return [i+1,j+1]
       elif tot<target:
         i+=1
       else:
        j-=1
      return [-1,-1]    
