def solve(s):
    counter = 0
    i = 0
    
    
    while i < len(s):
        if int(s[i]) % 2 != 0:
            counter += 1

        
        j = i + 1
        
        while j < len(s):
            if int(s[i:j + 1]) % 2 != 0:
                counter += 1

            j += 1
                
        i += 1
    
    return counter