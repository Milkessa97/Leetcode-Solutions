
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapDiff = defaultdict(int) 
        for i in range(len(nums)):
            if nums[i] in mapDiff:
                return [mapDiff[nums[i]],i]
            mapDiff[target-nums[i]]=i