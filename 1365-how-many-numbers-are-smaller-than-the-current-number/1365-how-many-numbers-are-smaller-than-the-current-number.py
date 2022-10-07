class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)

        result = []

        for i in nums:
            result.append(num.index(i))
            
        return result