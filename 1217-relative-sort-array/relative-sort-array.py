class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        for i in arr2:
            res.extend([i]*freq[i])
            freq[i] = 0
        remains = []
        for num in freq:
            remains.extend([num]*freq[num])
        res.extend(sorted(remains))
        return res