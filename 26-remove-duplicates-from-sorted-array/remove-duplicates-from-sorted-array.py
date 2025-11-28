class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        PH=0
        for seeker in range(len(nums)):
            if nums[seeker]!=nums[PH]:
               PH+=1
               nums[PH]=nums[seeker]
            
        return PH+1
            