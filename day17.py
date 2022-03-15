def scale(strng, k, v):
    substring_list = strng.split()
    scaled_string = ""
    
    if strng == '':
        return ''
    
    for substring in substring_list:
        scaled_substring = ""
        for character in substring:
            counter = k
            while counter > 0:
                scaled_substring += character
                counter -= 1
                   
        rep = v
        while rep > 0:
            scaled_string += scaled_substring + "\n"
            rep -= 1    
        
    
    return scaled_string.rstrip("\n")