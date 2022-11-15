class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dct = defaultdict(int)
        
        for c in s+t:
            dct[c] += 1
        
        for item in dct.items():
            if item[1] % 2 == 1:
                return item[0]