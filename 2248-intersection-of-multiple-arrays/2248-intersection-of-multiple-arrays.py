class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dct = defaultdict(int)

        arr = []

        for num in nums:
            for n in num:
                dct[n] += 1

        for item in dct.items():
            if (item[1] % len(nums) == 0):
                arr.append(item[0])

        arr.sort()
        
        return arr