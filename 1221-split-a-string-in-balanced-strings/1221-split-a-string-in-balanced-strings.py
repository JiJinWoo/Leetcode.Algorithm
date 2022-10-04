class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        check = 0
        for i in s:
            if i == "R":
                check += 1
            elif i == "L":
                check -= 1
            if check == 0:
                count += 1
        return count