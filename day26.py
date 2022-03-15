def count_deaf_rats(town):
    piper = town.index("P")
    deaf_rats = 0
    index = 0
    
    while index < len(town):
        if index == piper:
            index += 1
        elif index < piper:
            if town[index] == '~' and town[index + 1] == 'O':
                print("Rat is not deaf")
                index += 2
            elif town[index] == 'O' and town[index + 1] == '~':
                deaf_rats += 1
                index += 2
            else:
                index +=1
        elif index > piper:
            if town[index] == 'O' and town[index + 1] == '~':
                print("Rat is not deaf")
                index += 2
            elif town[index] == '~' and town[index + 1] == 'O':
                deaf_rats += 1
                index += 2
            else:
                index +=1
        else:
            index += 1
            
        
    
    return deaf_rats