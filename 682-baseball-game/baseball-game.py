class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=0
        stack=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                if i=='D':
                    stack.append(2*stack[-1])
                elif i=='C':
                    stack.pop()
                else:
                    stack.append(stack[-1]+stack[-2])
        return sum(stack)