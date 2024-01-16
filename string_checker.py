def is_valid_string(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack
print(is_valid_string("()"))      
print(is_valid_string("([])"))     
print(is_valid_string("{[()]}"))   
print(is_valid_string("abc"))    
print(is_valid_string("("))         
print(is_valid_string(")"))       
print(is_valid_string("(]"))        
print(is_valid_string("{[)}"))      













