def sortStation(strOfNumAndOper):
    
    strOfNumAndOper = strOfNumAndOper.replace(' ', '')
    
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output, stack = [], []
    
    newStrOfNumAndOper = []
    i = 0
    
    while i < len(strOfNumAndOper):
        if strOfNumAndOper[i].isdigit():
            num = strOfNumAndOper[i]
            while i+1 < len(strOfNumAndOper) and strOfNumAndOper[i+1].isdigit():
                i += 1
                num += strOfNumAndOper[i]
            newStrOfNumAndOper.append(num)
        else:
            newStrOfNumAndOper.append(strOfNumAndOper[i])
        i += 1
    
    for symbol in newStrOfNumAndOper:
        if symbol.isdigit():
            output.append(symbol)
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[symbol] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(symbol)
            
    return output + stack[::-1]

def reading(strOfNumAndOper):
    
    stack = []
    
    for symbol in strOfNumAndOper:
        if symbol in '+-*/^':
            b = stack.pop()
            a = stack.pop()
            
            if symbol == '/' and b == 0:
                return "/0"
            if symbol == '+': stack.append(a + b)
            elif symbol == '-': stack.append(a - b)
            elif symbol == '*': stack.append(a * b)
            elif symbol == '/': stack.append(a / b if b != 0 else float('inf'))
            elif symbol == '^': stack.append(a ** b)
        else:
            stack.append(float(symbol))
    
    return stack[0]
    
s = str(input())
print(reading(sortStation(s)))
