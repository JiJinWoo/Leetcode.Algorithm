class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_split = text.split(" ")
        
        result = 0
        
        for t in text_split:
            count = 0
            for b in brokenLetters:
                if b in t:
                    count = 1
                    break
            if not count:
                result += 1
                    

        return result