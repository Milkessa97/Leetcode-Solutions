class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num , count = nums[0] , 1
        for ind in range(1,len(nums)):
            if count == 0:
                num = nums[ind]
            if nums[ind] == num:
                count += 1
            else:
                count -= 1
        return num