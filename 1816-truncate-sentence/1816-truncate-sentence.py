class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence = s.split(' ')
        result = []
        for i in range(0, k):
            result.append(sentence[i])
        return ' '.join(result)