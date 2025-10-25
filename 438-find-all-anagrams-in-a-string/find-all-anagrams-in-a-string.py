class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:window])
        res = []
        for i in range(len(s)-window):
            if s_counter == p_counter:
                res.append(i)
            s_counter[s[i]] -= 1
            s_counter[s[i+window]] += 1
        if s_counter == p_counter:
            res.append(len(s)-window)
        return res