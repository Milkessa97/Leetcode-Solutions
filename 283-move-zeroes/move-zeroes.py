class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        PH=0
        for seeker in range(len(nums)):
            if nums[seeker]:
                nums[seeker],nums[PH]=nums[PH],nums[seeker]
                PH+=1