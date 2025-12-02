class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        point_g = 0
        point_s = 0
        while point_s < len(s):
            if point_g < len(g) and s[point_s] >= g[point_g]:
                count += 1
                point_g += 1
            point_s+=1
        return count

