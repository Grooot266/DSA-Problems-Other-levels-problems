class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointer sol
        vowels = "aeiouAEIOU"
        st=list(s)

        lpt=0
        rpt=len(st)-1

        while lpt < rpt : 
            if s[lpt] not  in vowels :
                lpt += 1 
            elif s[rpt] not in vowels :
                rpt -= 1
            else :
                st[lpt],st[rpt] = st[rpt],st[lpt]
                lpt += 1
                rpt -= 1

        return "".join(st)