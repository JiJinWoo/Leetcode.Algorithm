class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_dct = {}

        items = items1 + items2

        for l in items:
            if l[0] not in items_dct:
                items_dct[l[0]] = l[1]
            else:
                items_dct[l[0]] += l[1]


        result = sorted(items_dct.items())
        
        return result