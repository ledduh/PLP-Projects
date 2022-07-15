from datetime import date
import calendar
import datetime

date = date.today()
dates = date.weekday()
day = calendar.day_abbr[dates]

def fare():
    if 1 <= dates <= 5:
        print("Date: ", date,"\nDay: ", day,"\nFare: 100")
    elif dates == 6:
        print("Date: ", date,"\nDay: ", day,"\nFare: 60")
    elif dates == 0:
        print("Date: ", date,"\nDay: ", day,"\nFare: 80")
    else:
        print("Invalid")

fare()