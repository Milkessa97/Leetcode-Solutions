class NumArray:

    def __init__(self, nums: List[int]):
        self.l=[0]
        for i in nums:
            self.l.append(i+self.l[-1])
    def sumRange(self, left: int, right: int) -> int:
        return self.l[right+1]-self.l[left]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)