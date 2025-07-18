class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for i in s:
            if i == "}":
                if len(brackets) == 0:
                    return False
                last = brackets.pop()
                if last != "{":
                    return False
            elif i == ")":
                if len(brackets) == 0:
                    return False
                last = brackets.pop()
                if last != "(":
                    return False
            elif i == "]":
                if len(brackets) == 0:
                    return False
                last = brackets.pop()
                if last != "[":
                    return False
            else:
                brackets.append(i)

        if len(brackets) == 0:
            return True
        else:
            return False
