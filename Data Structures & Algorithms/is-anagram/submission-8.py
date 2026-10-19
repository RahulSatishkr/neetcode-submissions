class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        wordS = {}
        wordT = {}

        for char in s:
            wordS[char] = wordS.get(char,0)+1
    
        for char in t:
            wordT[char] = wordT.get(char,0)+1

        return wordS == wordT

        