import math
def stat(strg):
    if not strg:
        return ""
    
    races = strg.split(",")
    
    lengths = []
    
    results = ""
    
    
    for race in races:
        break_down = race.split('|')
        
        length = 0
        
        length += int(break_down[0]) * 60
        
        length += int(break_down[1])
        
        length += int(break_down[2]) / 60
        
        lengths.append(length)
        
       
    lengths.sort()
        
    range = max(lengths) - min(lengths)
    
    average = sum(lengths) / len(lengths)
    
    
    if len(lengths) % 2 == 0:
        mid = int(len(lengths) / 2)
        
        median = (lengths[mid - 1] + lengths[mid]) / 2
    else:
        mid = len(lengths) // 2
        
        median = lengths[mid]
        
    stats = [range, average, median]
    results = []
    
    for item in stats:
        hours = math.floor(item/60)
        minutes = int(item - (hours * 60))
        seconds = (item - (hours * 60) - minutes) * 60

        remainder = seconds - int(seconds)
        
        if remainder >= 0.98:
            seconds = round(seconds)
        else:
            seconds = math.floor(seconds)
        
        results.append("{:02d}|{:02d}|{:02d}".format(hours, minutes, seconds))
        
    return f"Range: {results[0]} Average: {results[1]} Median: {results[2]}"