class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        p1, p2 = 0, 0
        count = 0
        while p2 < len(heights):
            if heights[p2] != expected[p1]:
                count += 1
            p1 += 1
            p2 += 1
        return count