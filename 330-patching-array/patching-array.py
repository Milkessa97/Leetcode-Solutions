class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr_sum = 0
        patches = 0
        idx = 0
        ### the curr_sum variable tells us how many numbers can be created from the current index with it's patches included, if curr_sum=7, that means we made sure that all numbers upto 7 are possible to create with my current array
        while curr_sum < n and idx < len(nums):
            if nums[idx] <= curr_sum+1:
                curr_sum += nums[idx]
                idx += 1
            else:
                patches += 1
                curr_sum += curr_sum+1
        while curr_sum < n:
            curr_sum += curr_sum+1
            patches += 1
        return patches