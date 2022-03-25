def to_camel_case(text):
    if not text:
        return ''
    
    text_list = list(text)
    
    for i in range(len(text_list)):
        if text_list[i] in "_-":
            text_list[i] = ""
            text_list[i+1] = text[i+1].upper()
            
    return "".join(text_list)