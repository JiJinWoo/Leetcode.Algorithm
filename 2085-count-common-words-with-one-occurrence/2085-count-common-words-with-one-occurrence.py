class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dct = defaultdict(int)
        
        count = 0
        
        for word in words1+words2:
            dct[word] += 1
        
        for item in dct.items():
            if ((item[0] in words1) and (item[0] in words2)) and (item[1] == 2):
                    count += 1
                
        return count