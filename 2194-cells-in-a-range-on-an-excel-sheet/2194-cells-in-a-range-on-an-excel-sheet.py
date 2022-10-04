class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []

        row1 = int(s[1])
        row2 = int(s[4])
        col1 = ord(s[0])
        col2 = ord(s[3])

        for i in range(col1, col2 + 1):
            for j in range(row1, row2 + 1):
                result.append(f"{chr(i)}{j}")
        return result