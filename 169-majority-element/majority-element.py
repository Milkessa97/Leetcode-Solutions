class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_of_elements = Counter(nums)
        for num,freq in count_of_elements.items():
            if freq > len(nums)/2:
                return num