def in_array(array1, array2):
    r = []
    
    for i in array2:
        for j in array1:
            if j in i and j not in r:
                r.append(j)
            
    return sorted(r)