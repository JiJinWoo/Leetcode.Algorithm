class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        
        for num in nums:
            dct[num] += 1
            
        for item in dct.items():
            if item[1] >= len(nums)/2:
                return item[0]
        