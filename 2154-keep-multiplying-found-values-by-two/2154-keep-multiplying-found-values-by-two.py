class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numbers = set()
        for n in nums : numbers.add(n)

        while original in numbers : original *= 2

        return original;