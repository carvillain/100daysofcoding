def play_pass(s, n):
    alphabet = {"a": 1, "b": 2, "c": 3, "d":4, "e": 5,
               "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
               "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
               "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
               "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
               "z": 26}
    passphrase_list = []
    
    for character in s:
        if character.isalpha():
            character_value = alphabet[character.lower()] + n
            
            if character_value > 26:
                character_value = character_value - 26
                
            for key, value in alphabet.items():
                if value == character_value:
                    new_character = key
            
            passphrase_list.append(new_character)
        elif character in "0123456789":
            new_number = 9 - int(character)
            passphrase_list.append(str(new_number))
        else:
            passphrase_list.append(character)
    
    index = 0
    
    while index < len(passphrase_list):
        if index % 2 == 0 and passphrase_list[index].isalpha():
            passphrase_list[index] = passphrase_list[index].upper()
        
        index += 1
            
    
    return "".join(passphrase_list[::-1])