class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=Counter(s1)
        window=len(s1)
        newSet=Counter(s2[:window])
        left=0
        if newSet==s:
            return True
        while left<len(s2)-window:
            newSet[s2[left+window]]+=1
            newSet[s2[left]]-=1
            if newSet==s:
                return True
            left+=1
        return False
