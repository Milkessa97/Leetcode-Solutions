class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = [0]*len(arr1)
        idx = 0
        for i in arr2:
            while freq[i]!=0:
                res[idx] = i
                idx += 1
                freq[i] -= 1
        remains = []
        for num in freq:
            remains.extend([num]*freq[num])
        remains.sort()
        for i in remains:
            res[idx] = i
            idx += 1
        return res