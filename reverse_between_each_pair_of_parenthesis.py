class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack =[]
        for char in s:
            if char == '(' or char.islower():
                stack.append(char)
            else:
                tmp = []
                for i in range(len(stack)):
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    tmp.append(stack.pop())
                for item in tmp:
                    stack.append(item)
        return "".join(stack)
