class Solution:
    def greatestLetter(self, s: str) -> str:
        lower_s = s.lower()
        lower_s = sorted(lower_s)
        
        for c in reversed(lower_s):
            if (c.upper() in s) and (c.lower() in s):
                return c.upper()
            
        return ""