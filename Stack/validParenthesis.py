def isValid(s):
    stack = []
    valid = {"}" :"{","]" : "[",")" : "("}

    for bracket in s :

        if bracket in valid and len(stack) != 0:
            if valid[bracket] != stack[-1] :
                return False
            else:
                stack.pop()  
        else:
            stack.append(bracket)

    if(stack):
        return False
    else:
        return True      
        