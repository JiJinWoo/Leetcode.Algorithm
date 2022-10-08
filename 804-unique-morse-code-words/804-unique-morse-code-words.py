class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for i in range(len(words)):
            s = ""
            word = words[i]
            for j in word:
                index = alphabet.index(j)
                s += morse[index]
            if s not in result:
                result.append(s)
        return len(result)