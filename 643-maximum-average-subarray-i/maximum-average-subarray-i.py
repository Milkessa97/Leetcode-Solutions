class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first=0
        _sum = sum(nums[:k])
        _max = _sum
        while first < len(nums)-k:
            _sum += nums[first+k]
            _sum -= nums[first]
            if _sum > _max:
                _max = _sum
            first+=1
        return _max/k