class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0
        print(nums)
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                count += right-left
                left += 1
            else:
                right-=1
        return count