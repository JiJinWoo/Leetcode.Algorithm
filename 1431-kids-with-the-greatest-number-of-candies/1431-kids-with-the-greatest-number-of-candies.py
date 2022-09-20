class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arry = []
        for i in range(len(candies)):
            if max(candies) <= candies[i] + extraCandies:
                arry.append(True)
            else:
                arry.append(False)
        return arry