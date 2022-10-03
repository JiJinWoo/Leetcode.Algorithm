class Solution:
    def sortSentence(self, s: str) -> str:
        str = s.split()
        result = []

        for i in range(len(str)):
            for j in range(len(str)):
                if i+1 == int(str[j][-1]):
                    result.append(str[j][:-1])
                    sentence = " ".join(result)
        return sentence