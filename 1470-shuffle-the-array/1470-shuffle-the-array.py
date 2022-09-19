class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        arry = list()
        for i in range(n):
            arry.append(nums1[i])
            arry.append(nums2[i])
        return arry