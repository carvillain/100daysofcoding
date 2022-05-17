def chmod_calculator(perm):
    permissions = {"user" : 0, "group" : 0, "other" : 0}
    return_value = ""
    
    for key, value in perm.items():
        perm_value = 0
        for character in value:
            if character == "r":
                perm_value += 4
            elif character =="w":
                perm_value += 2
            elif character == "x":
                perm_value += 1
        
        permissions[key] = perm_value
        
    for key in permissions.keys():
        return_value += str(permissions[key])
        
    return return_value