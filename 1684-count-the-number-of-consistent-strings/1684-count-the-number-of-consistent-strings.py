class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        count = 0
        for word in words:
            for w in word:
                if w not in a:
                    count += 1
                    break
        return (len(words) - count)