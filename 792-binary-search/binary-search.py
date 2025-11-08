class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        while left<right:
            middle=(right+left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            else:
                right=middle
        return -1