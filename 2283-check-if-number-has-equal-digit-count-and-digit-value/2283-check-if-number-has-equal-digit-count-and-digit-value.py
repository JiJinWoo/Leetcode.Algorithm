class Solution:
    def digitCount(self, num: str) -> bool:
        dct =defaultdict(int)
        
        for i in range(len(num)):
            dct[i] = int(num[i])
            if dct[i] != num.count(str(i)):
                return False
        return True