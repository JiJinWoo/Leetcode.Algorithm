class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        
        res = sorted(nums, key=nums.count)
        
        return res