class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dct = defaultdict(int)

        count = 0

        for i in nums:
            dct[i] += 1
            if dct[i] % 2 == 0:
                count += 1
        
        return len(nums) / 2 == count