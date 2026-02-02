class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        trial = float("inf")
        diff = float("inf")
        nums.sort()
        print(nums)
        for idx in range(len(nums)):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[idx]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return total
                if abs(total-target) < diff:
                    diff = abs(total-target)
                    trial = total
                print(total)
        return trial