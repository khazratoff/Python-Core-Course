class Solution:
    def isValid(self, s: str)->bool:
        charlist = []
        valid = False
        if s[0] == '{' or '[' or '(':
                for char in s:
                    if char == '{' or char == '(' or char == '[':
                        charlist.append(char)
                    if char == '}' and charlist[-1] == '{':
                        charlist.pop()
                    if char == ')' and charlist[-1] == '(':
                        charlist.pop()
                    if char == ']' and charlist[-1] == '[':
                        charlist.pop()
                if len(charlist) == 0:
                    return valid
                else:
                    return valid
        else:
            return valid

o = Solution()
print(o.isValid('}])'))
