def SortStation(S):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output, stack = [], []
    for s in S:
        if s.isdigit():
            output.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[s] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(s)
    return output + stack[::-1]

def Reading(S):
    stack = []
    for s in S:
        if s in '+-*/^':
            b = stack.pop()
            a = stack.pop()
            stack.append({'+': a+b, '-': a-b, '*': a*b, '/': a/b, '^': a**b}[s])
        else:
            stack.append(float(s))
    return stack[0]
    
s = str(input())
print(SortStation(s))
print(Reading(SortStation(s)))