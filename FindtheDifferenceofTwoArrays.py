class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct1 = []
        for n in nums1:
            if n not in nums2 and n not in distinct1:
                distinct1.append(n)
        distinct2 = []
        for n in nums2:
            if n not in nums1 and n not in distinct2:
                distinct2.append(n)
        return [distinct1, distinct2]
