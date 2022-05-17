import datetime

def get_day(day, is_leap): 
    
    if is_leap == False:
        year = 2010
    else:
        year = 2012
        
    adjusted_day = str(day).rjust(3 + len(str(day)), '0')
    
    start_date = datetime.date(year, 1, 1)
    
    result_date = start_date + datetime.timedelta(days = day - 1)
    
    return result_date.strftime("%B, %-d")