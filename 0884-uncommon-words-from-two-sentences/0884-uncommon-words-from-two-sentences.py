class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dct = defaultdict(int)

        res = []

        for word in s1.split(' ') + s2.split(' '):
            dct[word] += 1

        for item in dct.items():
            if (item[1] == 1):
                res.append(item[0])
        
        return res