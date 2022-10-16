class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from string import ascii_lowercase

        alphabet_list = list(ascii_lowercase)

        same = []

        for i in sentence:
            if i not in same:
                same.append(i)

        same.sort()

        if same == alphabet_list:
            return True
        else:
            return False