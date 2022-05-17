def solution(s):
    s_length = len(s)
    result = []
    index = 0
    
    if s_length == 0:
        return result
    
    while index < s_length:
        if index == s_length - 1 and s_length % 2 != 0:
            result.append(f"{s[index]}_")
        else:
            result.append(f"{s[index]}{s[index + 1]}")
            
        index += 2
        
    return result