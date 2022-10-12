class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        nums1 = 1
        nums2 = 1

        for i in range(1, 3):
            nums1 *= nums[i-1]
            nums2 *= nums[-i]
        return (nums2 - nums1)