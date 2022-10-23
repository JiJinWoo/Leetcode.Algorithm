class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Basic Python function to determine the minimum number of operations
        required to collect the nums array of 0's. 
        
        :param nums: a list of non negative integers. (List[int])
        :return iterations: the number of iterations required. (int)
        """
        
        def helper(nums: List[int]) -> List[int]:
            """Helper function to sort and find minimum val > 0."""
            numbers = [x for x in nums if x > 0]
            nums = [(x-min(numbers)) if x > 0 else 0 for x in nums]
            return nums
        
        iterations = 0
        while max(nums) > 0:
            nums = helper(nums)
            iterations += 1
        
        return iterations