class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        if numOnes >= k:
            total += k
        else:
            total += numOnes
            k -= numOnes
            k -= numZeros
            if k>0:
                total += k*(-1)
        return total