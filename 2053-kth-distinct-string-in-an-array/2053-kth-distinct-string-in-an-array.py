class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = []

        for c in arr:
            if arr.count(c) == 1:
                result.append(c)

        if len(result) < k:
            return ""
        else:
            return result[k-1]