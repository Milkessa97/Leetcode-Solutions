class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        for i in costs:
            i.append(i[0]-i[1])
        costs.sort(key=lambda x: (x[2]))
        res=0
        for i in range(n):
            if i<(n/2):
                res+=costs[i][0]
            else:
                res+=costs[i][1]
        return res
        