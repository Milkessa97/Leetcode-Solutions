class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pointer_g=0
        pointer_s=0
        count=0
        while pointer_s<len(s):
            if s[pointer_s]>=g[pointer_g]:
                count+=1
                pointer_s+=1
                pointer_g+=1
                if pointer_g==len(g):
                    return count
            else:
                pointer_s+=1
        return count