def assemble(arr):
    if not arr:
        return ''
    
    output = list(arr[0])
    
    for item in arr[1:]:
        index = 0
        while index < len(item):
            if item[index] != '*':
                if output[index] == '*':
                    output[index] = item[index]
            index += 1
                
    
    return "".join(output).replace("*", "#")