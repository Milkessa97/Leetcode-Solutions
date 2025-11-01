class Solution:
    def minimumSteps(self, s: str) -> int:
        l=list(s)
        ind=0
        count=0
        swaps=0
        while ind<len(l):
            if l[ind]=='1':
                count+=1
            else:
                swaps+=count
            ind+=1
        return swaps