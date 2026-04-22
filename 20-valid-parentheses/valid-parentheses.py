class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sy = {')':'(',']':'[','}':'{'}

        for ch in s :
            if ch in sy :
                if not stack or stack[-1] != sy[ch]:
                    return False
                stack.pop()
            else :
                stack.append(ch)
        return not stack


