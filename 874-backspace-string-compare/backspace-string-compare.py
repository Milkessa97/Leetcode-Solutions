class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_A = []
        stack_B = []

        for i in range(len(s)):
            if s[i] == '#':
                if stack_A:
                    stack_A.pop()
            else:
                stack_A.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if stack_B:
                    stack_B.pop()
            else:
                stack_B.append(t[i])

        return stack_A==stack_B
            