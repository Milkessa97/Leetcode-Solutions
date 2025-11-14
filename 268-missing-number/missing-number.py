class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        p=0
        while p<len(nums):
            if nums[p]!=p:
                return p
            p+=1
        else:
            return p