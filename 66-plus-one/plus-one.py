class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0,0)
        digits[-1] += 1
        idx = -1
        while idx > -len(digits):
            if digits[idx]==10:
                digits[idx]=0
                digits[idx-1]+=1
            idx -= 1
        if digits[0]==0:
            return digits[1:]
        else:
            return digits