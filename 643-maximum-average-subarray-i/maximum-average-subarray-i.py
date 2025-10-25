class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        currentSum = sum(nums[:k])
        maxSum = currentSum
        while i < len(nums)-k:
            currentSum += nums[i+k]
            currentSum -= nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
            i+=1
        return maxSum/k