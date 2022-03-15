def valid_braces(string):
    braces = []
    
    for item in string:
        if item in r"[{(":
            braces.append(item)
        else:
            if braces == []:
                return False
            elif item == r']':
                if '[' == braces[-1]:
                    braces.remove(r'[')
                else:
                    return False
            elif item == r")":
                if '(' == braces[-1]:
                    braces.remove(r'(')
                else:
                    return False
            elif item == r"}":
                if '{' == braces[-1]:
                    braces.remove(r"{")
                else:
                    return False
    if not braces:            
        return True
    else:
        return False