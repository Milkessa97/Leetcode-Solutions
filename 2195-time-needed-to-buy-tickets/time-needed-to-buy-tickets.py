class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        ind = 0
        n = len(tickets)
        while tickets[k]!=0:
            if tickets[ind%n]!=0:
                tickets[ind%n]-=1
                res+=1
            ind += 1
        return res