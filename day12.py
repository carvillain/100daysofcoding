def solution(n,d):
    
    list1 = [int(x) for x in str(n)]
    
    y = len(list1) - d
    
    if d <= 0:
        return []
    elif d > len(list1):
        return list1
    else:
        return list1[y:]