class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0

        for i in range(len(mat)):
            result += mat[i][i]
            if i != len(mat)-1-i:
                result += mat[i][len(mat)-1-i]
        return result