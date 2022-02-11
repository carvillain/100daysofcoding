def smash(words):
    string1 = ""
    for word in words:
        string1 += "".join(word) + " "
        
    return string1.rstrip()