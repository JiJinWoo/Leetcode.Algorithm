class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j = set(jewels)
        for i in stones:
            if i in j:
                count += 1
        return count