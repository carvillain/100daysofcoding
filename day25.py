def up_array(arr):
    str_value = ""
    new_arr = []
    
    if not arr:
        return None
    
    for item in arr:
        if item < 0 or item > 9:
            return None
        else:
            str_value += str(item)
            
    value = int(str_value) + 1
    
    if value < 0:
        return None
    
    for x in str(value):
        new_arr.append(int(x))
        
    return new_arr