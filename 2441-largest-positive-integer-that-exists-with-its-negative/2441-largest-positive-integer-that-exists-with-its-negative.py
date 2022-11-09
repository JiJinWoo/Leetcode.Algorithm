class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        for num in reversed(nums):
            if -(num) in nums:
                return num
        return -1