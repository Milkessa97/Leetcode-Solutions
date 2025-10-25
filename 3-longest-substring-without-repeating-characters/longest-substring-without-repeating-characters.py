class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        if not s:
            return 0
        if len(s)==1:
            return 1
        counter = Counter(s[left])
        uniqueCount = 0
        count = 1
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
                count -= 1
            count += 1
            uniqueCount = max(uniqueCount,count)
            right+=1
        return uniqueCount
