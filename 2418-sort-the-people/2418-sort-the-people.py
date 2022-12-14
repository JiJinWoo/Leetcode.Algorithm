class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_map = {}
        result = []

        for i in range(len(names)):
            hash_map[heights[i]] = names[i]

        sort_heights = sorted(hash_map.items(), reverse=True)

        for i in range(len(names)):
            result.append(sort_heights[i][1])
            
        return result