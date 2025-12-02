class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for idx in range(len(word)):
            if word[idx] != ch:
                stack.append(word[idx])
            else:
                stack.append(word[idx])
                res = ""
                for i in range(idx,-1,-1):
                    res += stack[i]
                return res+word[idx+1:]
        return word