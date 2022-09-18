class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        result = []
        for i in accounts:
            for j in i:
                sum += j
            result.append(sum)
            sum = 0
        result.sort()
        return result[-1]