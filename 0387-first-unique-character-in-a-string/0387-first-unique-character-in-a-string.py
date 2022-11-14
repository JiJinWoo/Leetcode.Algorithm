class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = defaultdict(int)
        
        for c in s:
            dct[c] += 1
            
        for item in dct.items():
            if item[1] == 1:
                return s.find(item[0])
        return -1