class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_dict = {"type": 0, "color": 1, "name": 2}

        key_index = key_dict[ruleKey]

        count = 0

        for item in items:
            if item[key_index] == ruleValue:
                count += 1

        return count