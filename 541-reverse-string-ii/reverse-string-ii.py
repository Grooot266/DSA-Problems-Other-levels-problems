class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0

        while i < len(s):

            first_part = s[i:i+k]
            result += first_part[::-1]

            second_part = s[i+k:i+2*k]
            result += second_part

          
            i += 2 * k

        return result