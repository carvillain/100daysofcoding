def well(arr):
    count = arr.count('good')
    
    if count == 0:
        msg = 'Fail!'
    elif count > 2:
        msg = 'I smell a series!'
    else:
        msg = 'Publish!'
        
    return msg 