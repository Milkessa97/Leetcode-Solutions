class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums=[nums[0]]
        for i in range(len(nums)):
            if nums[i]!=new_nums[-1]:
                new_nums.append(nums[i])
        a,b,c=0,1,2
        count=0
        print(nums)
        while c<len(new_nums):
            if new_nums[b]>new_nums[c] and new_nums[b]>new_nums[a]:
                count+=1
            elif new_nums[b]<new_nums[c] and new_nums[b]<new_nums[a]:
                count+=1
            a+=1
            b+=1
            c+=1
        return count