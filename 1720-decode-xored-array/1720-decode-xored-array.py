class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        xor = [first]
        for i in range(len(encoded)):
            xor.append(xor[i]^encoded[i])
        return xor