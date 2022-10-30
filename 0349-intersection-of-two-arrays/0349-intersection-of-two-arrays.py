class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for i in set(nums2):
            if i in set(nums1):
                result.append(i)
        return result