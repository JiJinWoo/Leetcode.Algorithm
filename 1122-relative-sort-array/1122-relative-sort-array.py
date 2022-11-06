class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = collections.Counter(arr1)
        keys = sorted(counter)
        
        res = []
        for n in arr2:
            if n in keys:
                res += [n] * counter[n]
                keys.remove(n)
        
        for k in keys:
            res += [k] * counter[k]
            
        return res