class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left = idx + 1
            right = len(nums)-1

            while left < right:
                if nums[idx] + nums[left] + nums[right] == 0:

                    res.append([nums[idx],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


                elif nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res
