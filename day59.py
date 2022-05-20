def solve(eq):
    value = 0
    left_value = 0
    multiplier = 1
    i = 0
    j = 0

    list1 = eq.split(" ")
    
    index_equal = list1.index('=')
    index_x = list1.index('x')
    
    # Forces an equation where x is always on the left side of evaluations for continuity
    if index_x < index_equal:
        right_side = list1[index_equal + 1:]
        left_side = list1[:index_equal]
    else:
        left_side = list1[index_equal + 1:]
        right_side = list1[:index_equal]
    
    while j < len(left_side):
        if left_side[j]  == "-":
            if left_side[j + 1] == "x":
                multiplier = -1
                j += 2
                
            else:
                right_side.append("+") 
                right_side.append(int(left_side[j+1]))
                j += 2
                
        elif left_side[j]  == "+":
            if left_side[j+1] == "x":
                j += 2
            else:
                right_side.append("-")
                right_side.append(int(left_side[j+1]))
                j += 2
        elif left_side[j] == "x":
            j += 1
        else:
            right_side.append("-")
            right_side.append(int(left_side[j]))
            j += 1
    
    while i < len(right_side):
        if right_side[i]  == "-":
            value -= int(right_side[i+1])
            i += 2
        elif right_side[i]  == "+":
            value += int(right_side[i+1])
            i += 2
        elif right_side[i] == '':
            i += 1
        else:
            value += int(right_side[i])
            i += 1
            

    return value * multiplier