inp = str(input())
outp = []
stack = []
k = 0
for i in inp:
    if i == '(':
        stack.append(i)
    if i == ')':
        outp.append(stack[-1])
        stack.pop(-1)
    if i.isdigit() and k == 0:
    
        outp.append(i)
    
    if i.isdigit() and k == 1:
        outp.append(i)
        outp.append(stack[-1])
        stack.pop(-1)
        outp.append(stack[-1])
        stack.pop(-1)
        k = 0
    
    if i == '*' or i == '/':
        stack.append(i)
        k = 1
    
    if i == '+' or i == '-':
        stack.append(i)
if '(' in outp:
    outp.remove('(')
if '(' in stack:
    stack.remove('(')
if len(stack) != 0:
    outp.append(stack[-1])
print(outp, stack)
    