class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Used combination two pointer and Sliding window technique method 
        if len(s1) > len(s2): return False #Early exit step 

        #Counting the letters of the s1 and the first wondow of s2
        s1_ct, s2_ct = [0]*26 ,[0]*26 

        for i in range(len(s1)):
            s1_ct[ord(s1[i]) - ord('a')] += 1 
            s2_ct[ord(s2[i]) - ord('a')] += 1

        
        #Counting how many letters got matched 
        matches = 0 
        for i in range(26):
            matches += (1 if s1_ct[i] == s2_ct[i] else 0)

        #Sliding the window across s2
        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26 : return True

            #Adding the new character s2[r]
            idx = ord(s2[r]) - ord('a')
            s2_ct[idx] += 1

            if s1_ct[idx] == s2_ct[idx]:
                matches += 1
            elif s1_ct[idx] + 1 == s2_ct[idx]:
                matches -= 1

            #Removing the old character s2[l]
            idx = ord(s2[l]) - ord('a')
            s2_ct[idx] -= 1

            if s1_ct[idx] == s2_ct[idx]:
                matches += 1
            elif s1_ct[idx] - 1 == s2_ct[idx]:
                matches -= 1
            l += 1 

        return matches == 26
