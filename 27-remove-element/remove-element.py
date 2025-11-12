class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        PH=0
        for seeker in range(PH,len(nums)):
            if nums[seeker]==val:
                if nums[seeker]!=nums[PH]:
                    PH=seeker
            else:
                nums[PH],nums[seeker]=nums[seeker],nums[PH]
                PH+=1
        return PH
            