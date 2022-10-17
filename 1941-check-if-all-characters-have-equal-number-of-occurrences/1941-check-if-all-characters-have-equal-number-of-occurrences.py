class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        result = []

        for i in s:
            result.append(s.count(i))

        if len(set(result)) == 1:
            return True
        else:
            return False