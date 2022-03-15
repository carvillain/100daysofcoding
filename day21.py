def high(x):
    list_of_words = x.split()
    word_scores = {}
    
    for word in list_of_words:
        word_score = 0
        
        for letter in word:
            word_score += ord(letter) - 96
        
        word_scores[word] = word_score
    
    highest_score = ""
    score = 0
    
    for key in word_scores.keys():
        if word_scores[key] > score:
            highest_score = f"{key}"
            score = word_scores[key]
    
    return highest_score