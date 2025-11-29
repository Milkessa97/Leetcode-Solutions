class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            twoSum=nums[i-1]+nums[i-2]
            if nums[i]<twoSum:
                return nums[i]+twoSum
        return 0