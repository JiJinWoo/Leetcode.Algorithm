class Solution:
    def countPoints(self, rings: str) -> int:
        r = []
        b = []
        g = []
        count = 0
        for i in range(0,len(rings),2):
            if rings[i] == 'R':
                r.append(int(rings[i+1]))
            elif rings[i] == 'B':
                b.append(int(rings[i+1]))
            elif rings[i] == 'G':
                g.append(int(rings[i+1]))
        for i in range(0,10):
            if (i in r) and (i in g) and (i in b):
                count = count + 1
        return count