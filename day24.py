def is_language_diverse(lst): 
    python = 0
    ruby = 0
    js = 0
    
    for dev in lst:
        if dev['language'] == 'Python':
            python += 1
        elif dev['language'] == 'Ruby':
            ruby += 1
        else:
            js += 1
            
    if python <= 2 * ruby and python <= 2 * js and ruby <= 2 * js and ruby <= 2 * python and js <= 2 * ruby and js <= 2 * python:
        return True
            
    return False