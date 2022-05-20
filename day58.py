def longest_consec(strarr, k):
    n = len(strarr)
    arr1 = []
    result = ""
    
    if n == 0 or k > n or k < 1:
        return ""
    
    if k == 1:
        arr1 = strarr
                
    else:
        for i in range(len(strarr) - k + 1):
            arr1.append("".join(strarr[i:i+k]))
        
    for item in arr1:
        if len(item) > len(result):
                result = item
    
    return result