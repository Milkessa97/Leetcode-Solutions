class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr=0
        for i in arr:
            k -= (i-curr)-1
            curr=i
            if k<=0:
                return k+curr-1
        return k+arr[-1]
