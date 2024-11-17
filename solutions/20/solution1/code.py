class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in dic:
                if not stack:
                    return False

                bracket = stack.pop()
                if dic[c] != bracket:
                    return False
            else:
                stack.append(c)

        return not stack