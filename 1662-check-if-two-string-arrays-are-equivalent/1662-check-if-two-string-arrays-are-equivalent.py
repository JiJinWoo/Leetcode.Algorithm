class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_result = ""
        word2_result = ""
        for word in word1:
            word1_result += word

        for word in word2:
            word2_result += word

        if word1_result == word2_result:
            return True
        else:
            return False