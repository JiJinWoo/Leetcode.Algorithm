class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1 = []
        for i in range(int(len(nums)/2)):
            freq = nums[2 * i]
            val = nums[2 * i + 1]
            for j in range(freq):
                list1.append(val)
        return list1