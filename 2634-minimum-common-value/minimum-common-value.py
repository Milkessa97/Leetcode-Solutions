class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pt_1, pt_2 = 0, 0
        while pt_1 < len(nums1) and pt_2 < len(nums2):
            if nums1[pt_1] == nums2[pt_2]:
                return nums1[pt_1]
            elif nums1[pt_1] < nums2[pt_2]:
                pt_1 += 1
            else:
                pt_2 += 1
        return -1