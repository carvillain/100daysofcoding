import datetime

def friday_the_thirteenths(start, end = None):
    freaky_fridays = []
    
    if end == None:
        end = start + 1
    else:
        end = end + 1
        
    for year in range(start, end):
        for month in range(1, 13):
            if datetime.datetime(year, month, 13).weekday() == 4:
                freaky_fridays.append("{}/{}/{}".format(month, 13, year))
            
    return " ".join(freaky_fridays)