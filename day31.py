def persistence(n):
    num_persist = 0
    
    if len(str(n)) == 1:
        return num_persist
    
    num = n
    
    while len(str(num)) > 1:
        
        product = 1
        
        for digit in list(str(num)):
            product *= int(digit)
            
        num = product
        num_persist += 1
        
    return num_persist