class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = []
        for i in range(len(sentences)):
            result.append(sentences[i].count(" ") + 1)
        result.sort()
        return result[-1]
