def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    
    birds2 = []
    for x in birds:
        if x not in geese:
            birds2.append(x)
            
    return birds2