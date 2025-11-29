class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind,PH=0,0
        prev=nums[PH]
        if len(nums)==1:
            return True
        if nums[PH]==0:
            return False
        while ind<len(nums):
            ind+=1
            nums[PH]-=1
            if ind==len(nums)-1:
                return True
            if nums[ind]:
                if nums[ind]>=nums[PH]:
                    PH=ind
                else:
                    if nums[PH]>=0:
                        if nums[PH]==len(nums)-1:
                            return True
                    else:
                        return False
            else:
                if nums[PH]==0:
                    return False
