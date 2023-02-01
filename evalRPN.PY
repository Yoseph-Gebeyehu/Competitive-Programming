class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        
        for i in tokens:
            if i.isdigit():
                stack.append(i)
            elif i.startswith('-') and i[1:].isdigit():
                stack.append(i)          
            else:
                a = stack.pop() 
                b = stack.pop()  
                c = int(eval(f'{b} {i} {a}'))
                stack.append(c)
        return int(stack[0])
