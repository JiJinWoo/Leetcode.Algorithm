class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = defaultdict(int)
        
        for num in nums:
            dct[num] += 1
            if dct[num] == 2:
                return True
        return False