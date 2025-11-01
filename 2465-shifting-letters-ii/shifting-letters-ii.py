class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = [0] * (len(s) + 1)
        for i in shifts:
            if i[2] == 0:
                l[i[0]] -= 1
                l[i[1] + 1] += 1
            else:
                l[i[0]] += 1
                l[i[1] + 1] -= 1
        prefixSum=[l[0]]
        for i in range(1,len(s)):
            prefixSum.append(prefixSum[-1] + l[i])
        s2=[]
        for i in range(len(s)):
            newC=((ord(s[i]) - ord('a') + prefixSum[i])) % 26 + ord('a')
            s2.append(chr(newC))
        return(''.join(s2))

