def order(sentence):
    if not sentence:
        return sentence
    
    new_sentence = []
    words = sentence.split()
    marker = 1
    
    while marker <= len(words):
    
        for word in words:

            if str(marker) in word:
                new_sentence.append(word)
                marker += 1
        
    return " ".join(new_sentence)