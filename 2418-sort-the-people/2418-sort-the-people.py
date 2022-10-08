class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        result = []

        sort_heights = sorted(heights, reverse=True)

        for i in sort_heights:
            index = heights.index(i)
            result.append(names[index])
            
        return result