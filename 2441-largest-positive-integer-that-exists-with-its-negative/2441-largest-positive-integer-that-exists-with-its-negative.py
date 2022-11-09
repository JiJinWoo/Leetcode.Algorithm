class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        abs_nums = []
        
        count = -1

        for num in nums:
            abs_nums.append(abs(num))

        abs_nums.sort()

        for num in abs_nums:
            if abs_nums.count(num) >= 2:
                if (num in nums) and (-(num) in nums):
                    count = num
                    
        return count