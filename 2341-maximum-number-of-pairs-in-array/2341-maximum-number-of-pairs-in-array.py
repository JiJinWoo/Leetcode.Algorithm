class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict = {}
        result = [0, 0]
        
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        
        for i in dict.items():
            result[0] += i[1] // 2
            result[1] += i[1] % 2
        
        return result