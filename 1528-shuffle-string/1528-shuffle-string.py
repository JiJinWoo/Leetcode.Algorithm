class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
            a = [0] * len(indices)
            for i in range(len(indices)):
                a[indices[i]] = s[i]
            return "".join(a)