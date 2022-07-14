# 스택을 이용한 풀이
def is_valid(string):
    data = {')':'(', ']':'[', '}':'{'}
    stack = []
    for i in string:
        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if stack != []:
                top = stack.pop()
                if data[i] != top:
                    return False
            else:
                return False
    res = len(stack) == 0
    return res

# test
print(is_valid("()"))   # True
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))   # False
print(is_valid("([)]"))   # Flase
print(is_valid("{[]}"))   # True
print(is_valid("((()))[]"))   # True
print(is_valid("]]"))   # False
