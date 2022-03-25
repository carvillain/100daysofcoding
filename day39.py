import calendar
import datetime

def most_frequent_days(year):
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
    first_of_the_year = datetime.datetime(year, month = 1, day = 1).strftime("%A")
    
    day = days_of_the_week.index(first_of_the_year)
    
    if calendar.isleap(year):
        if day == 6:
            return [days_of_the_week[0], days_of_the_week[day]]
        else:    
            return [days_of_the_week[day], days_of_the_week[day + 1]]
    else:
        return [first_of_the_year]