class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}

        result = 0

        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 0
            else:
                dict[nums[i]] += 1

        for item in dict.items():
            if item[1] == 0:
                result += item[0]
                
        return result