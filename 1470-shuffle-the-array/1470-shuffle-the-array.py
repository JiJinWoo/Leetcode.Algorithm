class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arry = []
        for i in range(n):
            arry.append(nums[i])
            arry.append(nums[i+n])
        return arry