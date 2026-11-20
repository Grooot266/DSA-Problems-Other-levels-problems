class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Hash table method sol
        #Checking if the length are matching or not 
        if len(s) != len(t):
            return False
        #Creating two empy dictionaryt
        S= {}
        T = {}
        
        #Looping characters of two string in one loop and return result if both the characters of strings are matched
        for i in range(len(t)):
            S[s[i]] = 1 + S.get(s[i],0)
            T[t[i]] = 1 + T.get(t[i],0)

        return S==T