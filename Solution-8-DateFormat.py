#Solution for problem 8
#referances https://stackoverflow.com/a/18944849
    #%a  Locale’s abbreviated weekday name.
    #%A  Locale’s full weekday name.      
    #%b  Locale’s abbreviated month name.     
    #%B  Locale’s full month name.
    #%c  Locale’s appropriate date and time representation.   
    #%d  Day of the month as a decimal number [01,31].    
    #%f  Microsecond as a decimal number [0,999999], zero-padded on the left
    #%H  Hour (24-hour clock) as a decimal number [00,23].    
    #%I  Hour (12-hour clock) as a decimal number [01,12].    
    #%j  Day of the year as a decimal number [001,366].   
    #%m  Month as a decimal number [01,12].   
    #%M  Minute as a decimal number [00,59].      
    #%p  Locale’s equivalent of either AM or PM.
    #%S  Second as a decimal number [00,61].
    #%U  Week number of the year (Sunday as the first day of the week)
    #%w  Weekday as a decimal number [0(Sunday),6].   
    #%W  Week number of the year (Monday as the first day of the week)
    #%x  Locale’s appropriate date representation.    
    #%X  Locale’s appropriate time representation.    
    #%y  Year without century as a decimal number [00,99].    
    #%Y  Year with century as a decimal number.   
    #%z  UTC offset in the form +HHMM or -HHMM.
    #%Z  Time zone name (empty string if the object is naive).    
   # %%  A literal '%' character.
#import datetime lib
import datetime
import time

#create varible to hold date time
d_ =datetime.datetime.now()

day_ =d_.strftime("%d")

dayOfWeek = d_.strftime("%A") + ", " + d_.strftime("%B")+ " " + day_ + " "+d_.strftime("%Y") + " at "+ d_.strftime("%I:%M:%S %p")

print(dayOfWeek)


def foo(myDate):
    date_suffix = ["th", "st", "nd", "rd"]

    if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
        return date_suffix[myDate % 10]
    else:
        return date_suffix[0]

print(foo(2))