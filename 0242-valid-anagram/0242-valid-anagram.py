class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = defaultdict(int)
        dct_t = defaultdict(int)
        
        for c in s:
            dct_s[c] += 1

        for c in t:
            dct_t[c] += 1

        return dct_s == dct_t