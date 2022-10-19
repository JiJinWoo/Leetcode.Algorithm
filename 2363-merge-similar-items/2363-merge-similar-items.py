class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_dct = defaultdict(int)

        for l in items1+items2:
            items_dct[l[0]] += l[1]

        return sorted(items_dct.items())