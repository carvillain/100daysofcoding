def validate_word(word):
    character_count = []
    word = word.lower()
    
    for character in word:
        if character == word[0]:
            character_count.append(word.count(character))
        else:
            if word.count(character) not in character_count:
                character_count.append(word.count(character))
                return False
            else:
                pass
    return True