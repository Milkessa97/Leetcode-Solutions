class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        counter = defaultdict(int)
        uniqueCount = 0
        
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            uniqueCount = max(uniqueCount,right - left + 1)
            right+=1
        return uniqueCount
