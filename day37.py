import random

def shuffled_deck():
    suits = ['H', 'C', 'D', 'S']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []
    
    while len(deck) < 52:
        card_suit = random.randint(1,4) - 1
        card_value = random.randint(1,13) - 1
        
        random_card = f"{suits[card_suit]} {values[card_value]}"
        
        if random_card not in deck:
            deck.append(random_card)
    
    return deck