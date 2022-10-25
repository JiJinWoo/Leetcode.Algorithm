class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = defaultdict(int)
        for i in arr:
            dct[i] += 1
        return len(set(arr))==len(set(dct.values()))