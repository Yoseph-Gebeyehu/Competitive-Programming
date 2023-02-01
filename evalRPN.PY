class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        
        for i in tokens:
            if i.isdigit():
                stack.append(i)
            elif i.startswith('-') and i[1:].isdigit():
                stack.append(i)          
            else:
                a = stack.pop() #9
                b = stack.pop() #3 
                c = int(eval(f'{b} {i} {a}'))
                stack.append(c)
        return int(stack[0])
