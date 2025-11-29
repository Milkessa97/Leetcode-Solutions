class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a,b,c=0,1,2
        while c<len(nums):
            if nums[a]>=nums[b]+nums[c]:
                a+=1
                b+=1
                c+=1
            else:
                return nums[a]+nums[b]+nums[c]
        return 0